from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd
import pickle
import joblib

# Load preprocessing pipeline and model
processed1 = joblib.load('processed1')  # Assuming processed1 includes imputation and scaling
model = pickle.load(open('agglomerative_clustering_model.pkl', 'rb'))  # Agglomerative Clustering model


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST' :
        f = request.files['file']
        user = request.form['user']
        pw = request.form['password']
        db = request.form['databasename']
        engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")
        try:

            data = pd.read_csv(f)
        except:
                try:
                    data = pd.read_excel(f)
                except:      
                    data = pd.DataFrame(f)
                  
        # Drop the unwanted features
        univ_df = data.drop(["UnivID", "Univ",'State'], axis = 1)

        numeric_features = univ_df.select_dtypes(exclude = ['object']).columns
        data1 = pd.DataFrame(processed1.transform(univ_df[numeric_features]), columns = numeric_features)
        prediction = pd.DataFrame(model.fit_predict(data1), columns = ['Tier'])
        # Replace cluster_id values with tier labels
        prediction['Tier'] = prediction['Tier'].replace({0: 'Tier1', 1: 'Tier2'})
        prediction = pd.concat([prediction, data], axis = 1)
        
        prediction.to_sql('university_pred_kmeans', con = engine, if_exists = 'append', chunksize = 1000, index = False)
        
        html_table = prediction.to_html(classes = 'table table-striped')
        
        return render_template("data.html", Y = f"<style>\
                    .table {{\
                        width: 50%;\
                        margin: 0 auto;\
                        border-collapse: collapse;\
                    }}\
                    .table thead {{\
                        background-color: #39648f;\
                    }}\
                    .table th, .table td {{\
                        border: 1px solid #ddd;\
                        padding: 8px;\
                        text-align: center;\
                    }}\
                        .table td {{\
                        background-color: #888a9e;\
                    }}\
                            .table tbody th {{\
                            background-color: #ab2c3f;\
                        }}\
                </style>\
                {html_table}")



if __name__=='__main__':
    app.run(debug = True)

# EduCluster-Simplifying-University-Selection
## Overview
EduCluster is a data-driven application designed to assist international students in identifying suitable universities based on important criteria such as SAT scores, top 10 rankings, acceptance rates, student-faculty ratio, expenses, and graduation rates. The project leverages clustering algorithms to group universities with similar characteristics, making it easier for students to make informed decisions.

## <font color="green">Objective(s): Maximize the convenience of admission process.</font>
## <font color="green">Constraints: Minimize the brain drain.</font>

## *`CRISP-ML(Q)`* process model describes six phases:
### 1. Business and Data Understanding
### 2. Data Preparation
### 3. Model Building
### 4. Evaluation
### 5. Deployment
### 6. Monitoring and Maintenance

## <font color = 'darkblue'>Success Criteria:</font>
### `Business Success Criteria:` Reduce the application process time from anywhere between 20% to 40%
### `ML Success Criteria:` Achieve Silhoutte coefficient of atleast 0.5
### `Economic Success Criteria:` US Higher education department will see an increase in revenues by atleast 30%

## <font color = 'darkblue'>Features:</font>
### `University Clustering`: Uses hierarchical (agglomerative) and KMeans clustering algorithms.
### `Model Selection`: The best model is selected based on silhouette scores.
### `Data Integration`: Uses SQLAlchemy with MySQL for efficient data management.
### `Web Application`: A Flask web application that takes a list of colleges from a sheet and clusters them into Tier 1 and Tier 2 universities.
## Installation
1. **Clone the Repository**:

    `git clone https://github.com/MounikaGandla-01/EduCluster-Simplifying-University-Selection.git`
    
2. **Set Up Virtual Environment**:
    
   `python3 -m venv venv`

   `source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:
   
   `pip install -r requirements.txt`

4. **Configure MySQL Database**:
   Ensure you have a MySQL database setup. Update the connection details in app.py as needed.

## Usage

1. **Run the Application**:
   `python app.py`
2. **Access the Web Application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`
3. **Upload College List**: 
   Upload a sheet of colleges. The application will process the data and cluster the universities into Tier 1 and Tier 2.

## Project Structure
### `app.py`: Contains the main application code for the Flask web application.
### `templates/`: HTML templates for the web application.
### `test.xlsx`: Contains universities list for testing.
### `university_clustering.xlsx`: Source of universities used for clustering.
### `agglomerative_clustering_model.pkl`: Agglomerative clustering model file.
### `processed1`: Preprocessing pipeline including imputation and scaling.
### `University_clustering.ipynb`: Contains EDA, Descriptve Statistics and analysis based on various features.
### `venv/`: Virtual environment folder.
### `requirements.txt`: Lists the project dependencies.
### `README.md`: Project documentation.


## Data Collection
### Data:
### The university details are obtained from the US Higher Education Body and is publicly available for students to access.
### Dataset contains 25 university details
### 8 features are recorded for each university
### Description:
#### - Univ - University Name
#### - State - Location (state) of the university
#### - SAT - Cutoff SAT score for eligibility
#### - Top10 - % of students who ranked in top 10 in their previous academics
#### - Accept - % of students admitted to the universities
#### - SFRatio - Student to Faculty ratio
#### - Expenses - Overall cost in USD
#### - GradRate - % of students who graduate

## Clustering Algorithms
#### `Hierarchical (Agglomerative) Clustering`: Groups universities based on the hierarchical structure.
#### `KMeans Clustering`: Groups universities based on the centroid of clusters.
#### `Model Selection`: The best model Hierarchial Clustering is selected based on silhouette score of `0.552` to determine the optimal clustering.

## Evaluation:
#### `Silhouette Score`: Used to evaluate the quality of the clusters and select the best clustering algorithm.

## Flask Application
#### Routes
    Home Route (/)
    Renders the homepage.
#### Success Route (/success)
    Handles file upload, processes the data, performs clustering, and displays the results.


## Clustering Results

The following table presents the mean values of key metrics for universities clustered into Tier 1 and Tier 2:

| Cluster | SAT Score | Top 10 Rank (%) | Acceptance Rate (%) | Student-Faculty Ratio | Expenses (USD) | Graduation Rate (%) |
|---------|-----------|-----------------|---------------------|-----------------------|----------------|---------------------|
| Tier 1  | 1308.0    | 83.67           | 33.33               | 11.40                 | 30708.95       | 89.65               |
| Tier 2  | 1061.5    | 38.75           | 70.00               | 19.25                 | 9953.00        | 71.75               |

These clusters were derived using hierarchical (agglomerative) and  on university data sourced from the US Higher Education Body. The clustering aims to assist international students in making informed decisions by grouping universities with similar characteristics.

For detailed implementation and code, please refer to the project files and documentation provided.

# Bank-Customer-Churn-Prediction
A Machine Learning project to predict bank customer churn using Logistic Regression, Random Forest, and Gradient Boosting, with a FastAPI backend and Streamlit frontend.





Bank Customer Churn Prediction
A machine learning project that predicts whether a bank customer is
likely to leave (churn) based on customer information. It includes
exploratory data analysis, preprocessing, model training and evaluation,
a FastAPI prediction API, and a Streamlit user interface.

Features
Explore the customer dataset and inspect summary statistics and
missing values.

Visualize churn distribution and customer attributes with
Matplotlib.

Preprocess categorical features and scale input features.

Train classification models:

Logistic Regression

Random Forest Classifier

Gradient Boosting Classifier

Evaluate models using accuracy, precision, recall, F1-score, and a
confusion matrix.

Serve predictions through a FastAPI endpoint.

Enter customer details through a Streamlit interface and view the
predicted churn risk.

Tech Stack
Python

Pandas and NumPy

Matplotlib

scikit-learn

Joblib

FastAPI

Streamlit

Requests

Project Structure
.
├── app.py                         # Streamlit frontend
├── api.py                         # FastAPI prediction API
├── explore.py                     # Dataset overview and summary statistics
├── EDA.py                         # Exploratory data analysis and charts
├── preprocessing.py               # Encoding, train/test split, and scaling
├── train_logiticregretion.py.py   # Train Logistic Regression
├── train_random_forest.py         # Train Random Forest
├── train_gradient_boosting.py     # Train Gradient Boosting
├── evaluate.py                    # Evaluate saved models
├── scaler.joblib                  # Saved feature scaler
├── churn_model.joblib             # Saved Logistic Regression model
├── random_forest_model.joblib     # Saved Random Forest model
├── gradient_boosting_model.joblib # Saved Gradient Boosting model
└── Bank Customer Churn Prediction.csv
Setup
Clone this repository and open the project folder.

git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
Create and activate a virtual environment (recommended).

Windows

python -m venv .venv
.venv\Scripts\activate
macOS/Linux

python3 -m venv .venv
source .venv/bin/activate
Install the dependencies.

pip install pandas numpy matplotlib scikit-learn joblib fastapi uvicorn streamlit requests
Run the Project
Keep the terminal in the project folder.

1. Start the API
uvicorn api:app --reload
The API runs locally at http://127.0.0.1:8000. Interactive API
documentation is available at http://127.0.0.1:8000/docs.

2. Start the Streamlit interface
Open a second terminal, activate the same virtual environment, and run:

streamlit run app.py
The Streamlit app sends customer data to the API at
http://127.0.0.1:8000/predict.

Optional: Train the models
Run these commands from the project directory:

python train_logiticregretion.py.py
python train_random_forest.py
python train_gradient_boosting.py
To evaluate the saved models:

python evaluate.py
How It Works
Load the bank customer churn CSV dataset.

Encode categorical data and create country indicator columns.

Split the data into training and testing sets.

Scale the features and save the scaler.

Train classification models and save them with Joblib.

Send customer details from the Streamlit interface to the FastAPI
endpoint.

Return a churn prediction to the interface.

Important Notes
The model's predictions are estimates based on the training data,
not guarantees about an individual customer.

Keep the CSV dataset and required .joblib files in the project
directory when running the scripts.

Before publishing, verify that you have permission to redistribute
the dataset and consider whether to include the dataset and
serialized model files in GitHub. For larger files, use Git LFS or
provide dataset instructions instead.

Ensure the feature columns and preprocessing steps used by the API
exactly match those used during training. Check model evaluation
results before relying on predictions.

This project is for learning and demonstration; it should not be
used as the sole basis for financial or customer-retention
decisions.

Future Improvements
Add automated tests and input validation.

Compare model performance in a clearly reported results table.

Add a requirements.txt file for reproducible setup.

Improve error handling and configuration for the API URL.

Deploy the API and Streamlit app so they can be accessed online.

Author
Deepanshu

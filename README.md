# Bank-Customer-Churn-Prediction
A Machine Learning project to predict bank customer churn using Logistic Regression, Random Forest, and Gradient Boosting, with a FastAPI backend and Streamlit frontend.

# 🏦 Bank Customer Churn Prediction

A Machine Learning project that predicts whether a bank customer is likely to leave the bank using customer data and classification algorithms.

This project uses multiple Machine Learning models and provides a FastAPI backend with a Streamlit frontend for making predictions.

## 🚀 Features

- Exploratory Data Analysis (EDA)
- Data preprocessing and feature scaling
- Customer churn prediction
- Multiple Machine Learning algorithms
- Model evaluation and comparison
- REST API using FastAPI
- Interactive web interface using Streamlit
- Model saving and loading using Joblib

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib
- **Machine Learning:** Scikit-learn
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **API Server:** Uvicorn
- **Model Serialization:** Joblib

## 🤖 Machine Learning Models

This project uses the following classification algorithms:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

These models are used to predict customer churn based on customer information.

## 📂 Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── app.py
├── api.py
├── explore.py
├── EDA.py
├── preprocessing.py
├── train_logiticregretion.py.py
├── train_random_forest.py
├── train_gradient_boosting.py
├── evaluate.py
│
├── churn_model.joblib
├── random_forest_model.joblib
├── gradient_boosting_model.joblib
├── scaler.joblib
│
├── Bank Customer Churn Prediction.csv
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd Bank-Customer-Churn-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn joblib fastapi uvicorn streamlit requests
```

## ▶️ How to Run the Project

### Step 1: Start the FastAPI Backend

Open a terminal in the project directory and run:

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

To explore the API documentation, visit:

```text
http://127.0.0.1:8000/docs
```

### Step 2: Start the Streamlit Frontend

Open another terminal in the same project directory.

Activate the virtual environment if needed, then run:

```bash
streamlit run app.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser to use the application.

**Note:** Start the FastAPI backend before using the frontend. The API URL configured in `app.py` must match the address where the backend is running.

## 🧠 Model Training

To train the Logistic Regression model:

```bash
python train_logiticregretion.py.py
```

To train the Random Forest model:

```bash
python train_random_forest.py
```

To train the Gradient Boosting model:

```bash
python train_gradient_boosting.py
```

To evaluate the saved models:

```bash
python evaluate.py
```

Run these commands only after confirming that the required dataset, preprocessing code, and dependencies are available.

## 📊 Model Evaluation

Machine Learning models can be evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Actual model performance depends on the dataset, preprocessing, train-test split, and evaluation results.

## 🔄 Project Workflow

1. Load the customer churn dataset.
2. Explore the data and identify useful features.
3. Perform data preprocessing and encode categorical variables.
4. Split the data into training and testing sets.
5. Train classification models.
6. Evaluate model performance.
7. Save trained models using Joblib.
8. Start the FastAPI backend.
9. Use the Streamlit interface to submit customer information.
10. Display the churn prediction returned by the API.

## 🎯 Project Objective

The main objective of this project is to apply Machine Learning techniques to customer churn prediction and understand how data preprocessing, classification models, model evaluation, APIs, and frontend integration work together in an end-to-end project.

## 🔮 Future Improvements

- Improve model performance through hyperparameter tuning.
- Add more evaluation metrics and model comparisons.
- Improve the user interface.
- Add input validation and error handling.
- Create a requirements.txt file.
- Deploy the application online.
- Add automated tests.

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes. Predictions are estimates based on the available dataset and should not be treated as guaranteed outcomes.

## 👨‍💻 Author

**Deepanshu **

B.Tech CSE (AI & ML) Student

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and building AI-powered applications.

---

⭐ If you find this project useful, consider giving the repository a star!

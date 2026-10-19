# import joblib
# import pandas as pd
# from fastapi import FastAPI
# from pydantic import BaseModel
# model=joblib.load("gradient_boosting_model.joblib")
# scaler=joblib.load("scaler.joblib")
# app=FastAPI()

# @app.get("/")

# def home():
#     return{"message":"churn prediction"}


# class Customerdata(BaseModel):
#     customer_id:int
#     credit_score:int
#     gender:int
#     age:int
#     tenure:int
#     balance:float
#     products_number:int
#     credit_card:int
#     active_member:int
#     estimated_salary:float
#     country_Germany:int
#     country_Spain:int


# @app.post("/predict")
# def predict(data: Customerdata):

#     input_data = [[
#         data.credit_score,
#         data.gender,
#         data.age,
#         data.tenure,
#         data.balance,
#         data.products_number,
#         data.credit_card,
#         data.active_member,
#         data.estimated_salary,
#         data.country_Germany,
#         data.country_Spain
#     ]]

#     scaled_data = scaler.transform(input_data)

#     prediction = model.predict(scaled_data)

    
    
#     if prediction[0] == 1:
#        result = "Churn"
#     else:
#       result = "No Churn"

#     return {
#       "prediction": int(prediction[0]),
#       "result": result
# }


# import joblib
# import pandas as pd
# from fastapi import FastAPI
# from pydantic import BaseModel

# # Load trained model and scaler
# model = joblib.load("gradient_boosting_model.joblib")
# scaler = joblib.load("scaler.joblib")

# app = FastAPI()


# # Home endpoint
# @app.get("/")
# def home():
#     return {"message": "Churn Prediction API"}


# # Input data structure
# class Customerdata(BaseModel):
#     customer_id: int
#     credit_score: int
#     gender: int
#     age: int
#     tenure: int
#     balance: float
#     products_number: int
#     credit_card: int
#     active_member: int
#     estimated_salary: float
#     country_Germany: int
#     country_Spain: int


# # Prediction endpoint
# @app.post("/predict")
# def predict(data: Customerdata):

#     # Create input DataFrame
#     input_data = pd.DataFrame([[
#         data.credit_score,
#         data.gender,
#         data.age,
#         data.tenure,
#         data.balance,
#         data.products_number,
#         data.credit_card,
#         data.active_member,
#         data.estimated_salary,
#         data.country_Germany,
#         data.country_Spain
#     ]], columns=[
#         "credit_score",
#         "gender",
#         "age",
#         "tenure",
#         "balance",
#         "products_number",
#         "credit_card",
#         "active_member",
#         "estimated_salary",
#         "country_Germany",
#         "country_Spain"
#     ])

#     # Scale input
#     scaled_data = scaler.transform(input_data)

#     # Prediction
#     prediction = model.predict(scaled_data)

#     # Convert prediction to readable result
#     if prediction[0] == 1:
#         result = "Churn"
#     else:
#         result = "No Churn"

#     return {
#         "prediction": int(prediction[0]),
#         "result": result
#     }


import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load trained model and scaler
model = joblib.load("gradient_boosting_model.joblib")
scaler = joblib.load("scaler.joblib")

app = FastAPI()


# Home endpoint
@app.get("/")
def home():
    return {"message": "Churn Prediction API"}


# Input data structure
class Customerdata(BaseModel):
    customer_id: int
    credit_score: int
    gender: int
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float
    country_Germany: int
    country_Spain: int


# Prediction endpoint
@app.post("/predict")
def predict(data: Customerdata):

    # Create input DataFrame
    input_data = pd.DataFrame([[
        data.customer_id,
        data.credit_score,
        data.gender,
        data.age,
        data.tenure,
        data.balance,
        data.products_number,
        data.credit_card,
        data.active_member,
        data.estimated_salary,
        data.country_Germany,
        data.country_Spain
    ]], columns=[
        "customer_id",
        "credit_score",
        "gender",
        "age",
        "tenure",
        "balance",
        "products_number",
        "credit_card",
        "active_member",
        "estimated_salary",
        "country_Germany",
        "country_Spain"
    ])

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled_data)
    #probality
    probability = model.predict_proba(scaled_data)

    churn_probability = probability[0][1]

    confidence = max(probability[0]) * 100

    # Convert prediction to readable result
    if prediction[0] == 1:
        result = "Churn"
    else:
        result = "No Churn"

    return {
        "prediction": int(prediction[0]),
        "result": result,
        "churn_probability": round(float(churn_probability) * 100, 2),
        "confidence": round(float(confidence), 2)
    }



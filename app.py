import streamlit as st
import requests
st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦"
)

st.title("🏦 Bank Customer Churn Prediction")
st.write("Enter customer details to predict churn.")

# Customer ID
customer_id = st.number_input(
    "Customer ID",
    min_value=0,
    step=1
)

# Credit Score
credit_score = st.number_input(
    "Credit Score",
    min_value=0,
    max_value=1000,
    step=1
)

# Gender
gender = st.selectbox(
    "Gender",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

# Age
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    step=1
)

# Tenure
tenure = st.number_input(
    "Tenure",
    min_value=0,
    step=1
)

# Balance
balance = st.number_input(
    "Balance",
    min_value=0.0,
    step=100.0
)

# Number of Products
products_number = st.number_input(
    "Number of Products",
    min_value=0,
    step=1
)

# Credit Card
credit_card = st.selectbox(
    "Credit Card",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# Active Member
active_member = st.selectbox(
    "Active Member",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# Estimated Salary
estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    step=1000.0
)

# Germany
country_Germany = st.selectbox(
    "Country: Germany",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# Spain
country_Spain = st.selectbox(
    "Country: Spain",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)


# if st.button("🔮 Predict Churn"):

#     data = {
#         "customer_id": customer_id,
#         "credit_score": credit_score,
#         "gender": gender,
#         "age": age,
#         "tenure": tenure,
#         "balance": balance,
#         "products_number": products_number,
#         "credit_card": credit_card,
#         "active_member": active_member,
#         "estimated_salary": estimated_salary,
#         "country_Germany": country_Germany,
#         "country_Spain": country_Spain
#     }

#     response = requests.post(
#         "http://127.0.0.1:8000/predict",
#         json=data
#     )

#     result = response.json()

# if result["prediction"] == 1:
#     st.error("⚠️ Customer is likely to Churn")
# else:
#     st.success("✅ Customer is unlikely to Churn")

# col1, col2 = st.columns(2)

# with col1:
#     st.metric(
#         "Churn Probability",
#         f'{result["churn_probability"]}%'
#     )

# with col2:
#     st.metric(
#         "Model Confidence",
#         f'{result["confidence"]}%'
#     )

# st.subheader("Churn Risk")

# churn_probability = result["churn_probability"]

# col1, col2 = st.columns([4, 1])

# with col1:
#     st.progress(churn_probability / 100)

# with col2:
#     st.write(f"**{churn_probability}%**")
if st.button("🔮 Predict Churn"):

    data = {
        "customer_id": customer_id,
        "credit_score": credit_score,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary,
        "country_Germany": country_Germany,
        "country_Spain": country_Spain
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data,
            timeout=10
        )

        response.raise_for_status()

        result = response.json()

        if result["prediction"] == 1:
            st.error("⚠️ Customer is likely to Churn")
        else:
            st.success("✅ Customer is unlikely to Churn")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Churn Probability",
                f'{result["churn_probability"]}%'
            )

        with col2:
            st.metric(
                "Model Confidence",
                f'{result["confidence"]}%'
            )

        st.subheader("Churn Risk")

        churn_probability = result["churn_probability"]

        col1, col2 = st.columns([4, 1])

        with col1:
            st.progress(churn_probability / 100)

        with col2:
            st.write(f"**{churn_probability}%**")

        if churn_probability < 30:
            st.success("🟢 Low Risk")

        elif churn_probability <= 60:
            st.warning("🟡 Medium Risk")

        else:
            st.error("🔴 High Risk")
    except requests.exceptions.ConnectionError:
        st.error("❌ Prediction server is not running.")

    except requests.exceptions.Timeout:
        st.error("⏱️ Prediction server took too long to respond.")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('modelloan.joblib')

st.title("🏦 Loan Status Prediction App")
st.markdown("Fill in the applicant details below to predict the loan approval status.")

#Sidebar
# Sidebar
st.sidebar.title("🔍 About This Model")
st.sidebar.info("""
This model predicts whether loan will be **approved or rejected** based on applicant details.

- Model: Support Vector Machine Model(SVM) 
- Dataset: Loan Status Dataset from Kaggle
""")
st.sidebar.write("✨ Developed using **Streamlit**")

# Input widgets
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0.0, step=100.0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, step=100.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, step=10.0)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0.0, step=10.0)
credit_history = st.selectbox("Credit History", ["1", "0"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert categorical inputs to numeric values (as used during training)
gender_val = 1 if gender == "Male" else 0
married_val = 1 if married == "Yes" else 0
dependents_val = 3 if dependents == "3+" else int(dependents)
education_val = 1 if education == "Graduate" else 0
self_employed_val = 1 if self_employed == "Yes" else 0
credit_history_val = int(credit_history)

property_area_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}
property_area_val = property_area_map[property_area]

# Predict
if st.button("Predict Loan Status"):
    user_input = np.array([[gender_val, married_val, dependents_val, education_val, self_employed_val,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_amount_term, credit_history_val, property_area_val]])
    
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")

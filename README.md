# 🏦 Loan Status Prediction using SVM

This project uses a **Support Vector Machine (SVM)** model to predict the approval status of a loan application based on various features.
The model is trained on structured data and deployed using a **Streamlit web app** for user-friendly interaction.

## Features

- Predicts loan approval status (`Y` = Approved, `N` = Rejected)
- Trained using Support Vector Machine (SVM)
- Model saved and loaded using `joblib`
- Interactive web app interface with Streamlit
- Accepts real-time user input for predictions

## Input Features

The model uses the following input columns:

| Feature             | Type        | Description                                      |
|---------------------|-------------|--------------------------------------------------|
| Gender              | Categorical | Male / Female                                    |
| Married             | Categorical | Yes / No                                         |
| Dependents          | Categorical | 0 / 1 / 2 / 3+                                   |
| Education           | Categorical | Graduate / Not Graduate                          |
| Self_Employed       | Categorical | Yes / No                                         |
| ApplicantIncome     | Numerical   | Applicant's income                               |
| CoapplicantIncome   | Numerical   | Co-applicant's income                            |
| LoanAmount          | Numerical   | Loan amount (in thousands)                       |
| Loan_Amount_Term    | Numerical   | Term of loan (in days)                           |
| Credit_History      | Binary      | 1 = Good, 0 = Bad credit history                 |
| Property_Area       | Categorical | Urban / Semiurban / Rural                        |

## How to Use

### 1. Install Requirements

```bash
pip install -r requirements.txt

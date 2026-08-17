import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/credit_scoring_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Credit Scoring Model",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Scoring Prediction")
st.write(
    "Enter customer financial information to estimate credit risk."
)

st.divider()
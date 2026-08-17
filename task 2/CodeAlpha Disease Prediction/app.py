import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/disease_prediction_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Disease Prediction Model")

st.write(
    "Enter the medical measurements below to predict the tumor diagnosis."
)

st.divider()
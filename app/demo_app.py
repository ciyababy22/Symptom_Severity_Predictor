"""
Streamlit Demo Application for Symptom Severity Prediction
"""

import sys
import os
import streamlit as st

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.severity_predictor import SymptomSeverityPredictor

# Risk descriptions
RISK_DESCRIPTIONS = {
    "Low Risk": "Symptoms are mild. Monitor and rest.",
    "Moderate Risk": "Symptoms are moderate. Consider consulting a doctor.",
    "High Risk": "Symptoms are severe. Seek medical attention immediately."
}

# Initialize predictor
predictor = SymptomSeverityPredictor()

# Page configuration
st.set_page_config(
    page_title="Symptom Severity Predictor",
    page_icon="🩺",
    layout="centered"
)

# Header
st.title("🩺 Symptom Severity Predictor")
st.write(
    "Enter your symptoms separated by commas and "
    "receive a risk assessment."
)

# Input box
user_input = st.text_input(
    "Symptoms",
    placeholder="fever, cough, headache"
)

# Predict button
if st.button("Predict Severity"):

    symptoms = [
        symptom.strip()
        for symptom in user_input.split(",")
        if symptom.strip()
    ]

    if not symptoms:
        st.warning("Please enter at least one symptom.")
    else:

        risk = predictor.predict_severity(symptoms)

        st.subheader("Symptoms Summary")

        for symptom in symptoms:
            st.write(f"• {symptom.title()}")

        st.subheader("Prediction Result")

        if risk == "Low Risk":
            st.success(risk)
        elif risk == "Moderate Risk":
            st.warning(risk)
        else:
            st.error(risk)

        st.write("### Advice")
        st.info(RISK_DESCRIPTIONS[risk])

# Sidebar information
st.sidebar.header("About")
st.sidebar.write(
    "This prototype uses a rule-based scoring system "
    "to classify symptom severity."
)

st.sidebar.write(
    "Risk Levels:\n"
    "- Low Risk\n"
    "- Moderate Risk\n"
    "- High Risk"
)

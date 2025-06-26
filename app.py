# app.py

# --- Imports ---
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
from app1 import (
    init_granite_model,
    predict_disease,
    generate_treatment_plan,
    answer_patient_query
)

# --- Load .env Variables ---
load_dotenv()

# --- Load Custom CSS (Optional) ---
if "style.css" in os.listdir():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Page Config ---
st.set_page_config(page_title="HealthAI", layout="wide")
st.title("🧠 HealthAI: Smart Healthcare Assistant")

# --- Load Granite Model Once ---
model = init_granite_model()

# --- Feature 1: Patient Chat ---
def display_patient_chat(model):
    st.subheader("💬 Chat with AI Doctor")
    question = st.text_input("Ask your health question:")
    if st.button("Get Answer"):
        response = answer_patient_query(model, question)
        st.success(response)

# --- Feature 2: Disease Prediction ---
def display_disease_prediction(model):
    st.subheader("🔍 Disease Prediction from Symptoms")
    symptoms = st.text_area("Enter symptoms (comma-separated):", height=150)
    if st.button("Predict Disease"):
        prediction = predict_disease(model, symptoms)
        st.success(prediction)

# --- Feature 3: Treatment Plan Generator ---
def display_treatment_plans(model):
    st.subheader("🩺 Personalized Treatment Plan Generator")
    diagnosis = st.text_input("Enter the diagnosis:")
    age = st.number_input("Patient age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Select gender", ["Male", "Female", "Other"])
    if st.button("Generate Plan"):
        plan = generate_treatment_plan(model, diagnosis, age=age, gender=gender)
        st.success(plan)

# --- Feature 4: Health Analytics Dashboard ---
def display_health_analytics():
    st.subheader("📊 Health Data Analytics")
    st.info("This is a sample health dashboard. You can extend it with real patient data.")

    data = pd.DataFrame({
        "Disease": ["Dengue", "Typhoid", "Covid", "Malaria"],
        "Cases": [80, 55, 120, 40]
    })
    fig = px.bar(data, x="Disease", y="Cases", color="Disease", title="Reported Disease Cases")
    st.plotly_chart(fig, use_container_width=True)

# --- Sidebar Navigation ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose a feature:", [
    "💬 Patient Chat",
    "🔍 Disease Prediction",
    "🩺 Treatment Plan",
    "📊 Health Analytics"
])

# --- Display Selected Feature ---
if page == "💬 Patient Chat":
    display_patient_chat(model)
elif page == "🔍 Disease Prediction":
    display_disease_prediction(model)
elif page == "🩺 Treatment Plan":
    display_treatment_plans(model)
elif page == "📊 Health Analytics":
    display_health_analytics()

# app1.py

import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model

def init_granite_model():
    load_dotenv()
    api_key = os.getenv("WML_API_KEY")
    project_id = os.getenv("WML_PROJECT_ID")
    url = os.getenv("WML_URL")

    model = Model(
        model_id="ibm/granite-3-3-8b-instruct",
        params={"max_new_tokens": 100},
        credentials={"apikey": api_key, "url": url},
        project_id=project_id
    )
    return model

def predict_disease(model, symptoms):
    prompt = f"A patient reports the following symptoms: {symptoms}. What are the possible diseases?"
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']

def generate_treatment_plan(model, diagnosis, age=None, gender=None):
    patient_info = f"Diagnosis: {diagnosis}."
    if age: patient_info += f" Age: {age}."
    if gender: patient_info += f" Gender: {gender}."
    prompt = f"{patient_info} What is a suitable treatment plan?"
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']

def answer_patient_query(model, question):
    prompt = f"Patient asked: {question}"
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']

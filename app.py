import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Model
with open("health_condition_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

with open("frequency_maps.pkl", "rb") as f:
    freq_maps = pickle.load(f)

# Set Page Confiuration
st.set_page_config(
    page_title= 'Health Condition Prediction',
    page_icon= "🩺",
    layout= "wide"
)

st.title("🩺 Health Condition Prediction")

st.write("Predict whether a person's health condition is **At-Risk, Fit or Unhealthy** using Machine Learning.")

# Sidebar
st.sidebar.header("About")
st.sidebar.title("🩺 Health Condition Prediction")

st.sidebar.info("""
### 🤖 Model
CatBoost (Optuna Tuned)

### 📂 Dataset
Kaggle Playground Series S6E7

### 🏆 Kaggle Public Score
**0.90625**
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Model Performance")

col1, col2 = st.sidebar.columns(2)

with col1:
    st.metric("Balanced Accuracy", "0.9102")
    st.metric("Precision", "92.55%")
    st.metric("F1 Score", "89.31%")

with col2:
    st.metric("Accuracy", "88.11%")
    st.metric("Recall", "88.11%")
    st.metric("Macro F1", "76.12%")

st.sidebar.markdown("---")

st.sidebar.caption("Developed by Arnav Mandani")


# User Input

col1, col2 = st.columns(2)

with col1:

    sleep_duration = st.number_input(
        "Sleep Duration (Hours)",
        min_value = 0.0,
        max_value = 24.0,
        value = 7.0
    ) 

    heart_rate = st.number_input(
        "Heart Rate",
        value = 75.0
    )

    bmi = st.number_input(
        "BMI",
        value = 23.5
    )

    calorie_expenditure = st.number_input(
        "Calories Burned",
        value=400.0
    )

    step_count = st.number_input(
        "Step Count",
        value=8000.0
    )

    exercise_duration = st.number_input(
        "Exercise Duration (minutes)",
        value=45.0
    )

    water_intake = st.number_input(
        "Water Intake (liters)",
        value=2.5
    )

with col2:

    diet_type = st.selectbox(
        "Diet Type",
        ["Balanced", "High-Protein", "Vegetarian", "Vegan"]
    )

    stress_level = st.selectbox(
        "Stress Level",
        ["low", "medium", "high"]
    )

    sleep_quality = st.selectbox(
        "Sleep Quality",
        ["poor", "average", "good"]
    )

    physical_activity_level = st.selectbox(
        "Physical Activity",
        ["sedentary", "moderate", "active"]
    )

    smoking_alcohol = st.selectbox(
        "Smoking / Alcohol",
        ["No", "Yes"]
    )
    
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

# Feature Engineering

calorie_per_step = calorie_expenditure / max(step_count, 1)
water_per_bmi = water_intake / max(bmi, 1)
exercise_intensity = calorie_expenditure / (exercise_duration + 1)
steps_per_minute = step_count / (exercise_duration + 1)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

# Frequency Encoding Features

sleep_duration_freq = freq_maps["sleep_duration"].get(sleep_duration, 0)
heart_rate_freq = freq_maps["heart_rate"].get(heart_rate, 0)
bmi_freq = freq_maps["bmi"].get(bmi, 0)
calorie_expenditure_freq = freq_maps["calorie_expenditure"].get(calorie_expenditure, 0)
step_count_freq = freq_maps["step_count"].get(step_count, 0)
exercise_duration_freq = freq_maps["exercise_duration"].get(exercise_duration, 0)
water_intake_freq = freq_maps["water_intake"].get(water_intake, 0)
diet_type_freq = freq_maps["diet_type"].get(diet_type, 0)
stress_level_freq = freq_maps["stress_level"].get(stress_level, 0)
sleep_quality_freq = freq_maps["sleep_quality"].get(sleep_quality, 0)
physical_activity_level_freq = freq_maps["physical_activity_level"].get(
    physical_activity_level,
    0
)
smoking_alcohol_freq = freq_maps["smoking_alcohol"].get(
    smoking_alcohol,
    0
)
gender_freq = freq_maps["gender"].get(gender, 0)

# Prediction
if st.button("🔍 Predict Health Condition",use_container_width=True):

    input_df = pd.DataFrame({
        "sleep_duration":[sleep_duration],
        "heart_rate":[heart_rate],
        "bmi":[bmi],
        "calorie_expenditure":[calorie_expenditure],
        "step_count":[step_count],
        "exercise_duration":[exercise_duration],
        "water_intake":[water_intake],
        "diet_type":[diet_type],
        "stress_level":[stress_level],
        "sleep_quality":[sleep_quality],
        "physical_activity_level":[physical_activity_level],
        "smoking_alcohol":[smoking_alcohol],
        "gender":[gender],
        "calorie_per_step":[calorie_per_step],
        "water_per_bmi":[water_per_bmi],
        "bmi_category":[bmi_category],
        "exercise_intensity":[exercise_intensity],
        "steps_per_minute":[steps_per_minute],
        "sleep_duration_freq":[sleep_duration_freq],
        "heart_rate_freq":[heart_rate_freq],
        "bmi_freq":[bmi_freq],
        "calorie_expenditure_freq":[calorie_expenditure_freq],
        "step_count_freq":[step_count_freq],
        "exercise_duration_freq":[exercise_duration_freq],
        "water_intake_freq":[water_intake_freq],
        "diet_type_freq":[diet_type_freq],
        "stress_level_freq":[stress_level_freq],
        "sleep_quality_freq":[sleep_quality_freq],
        "physical_activity_level_freq":[physical_activity_level_freq],
        "smoking_alcohol_freq":[smoking_alcohol_freq],
        "gender_freq":[gender_freq]
    })

    prediction = model.predict(input_df).flatten()[0]

    if prediction == "fit":
        st.success(f"✅ Predicted Health Condition: **{prediction.title()}**")

    elif prediction == "at-risk":
        st.warning(f"⚠️ Predicted Health Condition: **{prediction.title()}**")

    else:
        st.error(f"🚨 Predicted Health Condition: **{prediction.title()}**")

    if hasattr(model, "predict_proba"):

        prob = model.predict_proba(input_df)[0]

        prob_df = pd.DataFrame({
            "Health Condition": model.classes_,
            "Probability": prob
        })

        st.subheader("Prediction Confidence")
        st.dataframe(prob_df, use_container_width=True)
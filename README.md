# 🩺 Student Health Condition Prediction

## 📌 Overview

This project is an **End-to-End Machine Learning Application** that predicts a student's health condition (**At-Risk**, **Fit**, or **Unhealthy**) based on lifestyle and health-related attributes.

The project covers the complete machine learning workflow, from data preprocessing and feature engineering to model training, hyperparameter tuning, deployment, and prediction using a Streamlit web application.

---

## 🎯 Problem Statement

The objective is to build a multiclass classification model that predicts a student's health condition using features such as:

- 😴 Sleep Duration
- ❤️ Heart Rate
- ⚖️ BMI
- 🔥 Calorie Expenditure
- 👣 Step Count
- 🏃 Exercise Duration
- 💧 Water Intake
- 🥗 Diet Type
- 😰 Stress Level
- 🌙 Sleep Quality
- 🏋️ Physical Activity Level
- 🚬 Smoking & Alcohol Habits
- 👤 Gender

---

## 📊 Dataset

- **Competition:** Kaggle Playground Series S6E7
- **Task:** Multiclass Classification
- **Target Variable:** `health_condition`

---

## 🚀 Project Workflow

```
Data Collection
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Feature Engineering
        │
        ▼
Data Preprocessing
        │
        ▼
Model Training
        │
        ▼
Hyperparameter Tuning (Optuna)
        │
        ▼
Final Model Selection
        │
        ▼
Model Deployment (Streamlit)
```

---

# 📊 Exploratory Data Analysis

- Missing Value Analysis
- Numerical Feature Analysis
- Categorical Feature Analysis
- Correlation Analysis
- Class Distribution
- Distribution Plots
- Boxplots
- Heatmaps

---

# ⚙️ Feature Engineering

Created several meaningful features including:

- Calories Burned per Step
- Water Intake per BMI
- Exercise Intensity
- Steps per Minute
- BMI Category

Frequency Encoding was also applied to improve model performance.

---

# 🔧 Data Preprocessing

- Ordinal Encoding
- One-Hot Encoding
- Frequency Encoding
- ColumnTransformer Pipeline

---

# 🤖 Models Trained

- Logistic Regression
- Decision Tree
- Random Forest
- Extra Trees
- XGBoost
- LightGBM
- CatBoost

---

# 🎯 Hyperparameter Tuning

Optuna was used for optimizing the best-performing models.

| Model | Trials |
|--------|--------|
| XGBoost | 50 |
| LightGBM | 20 |
| CatBoost | 20 |

---

# 🏆 Final Model Performance

| Metric | Score |
|---------|-------|
| Balanced Accuracy | **0.9102** |
| Accuracy | **88.11%** |
| Precision | **92.55%** |
| Recall | **88.11%** |
| F1 Score | **89.31%** |

---

# 🏅 Kaggle Result

**Public Leaderboard Score**

**0.90625**

---

# 💻 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- CatBoost
- XGBoost
- LightGBM
- Optuna
- Streamlit
- Matplotlib
- Plotly
- Git
- GitHub

---

# 🌐 Streamlit Demo

🔗 **Live Demo**

https://health-condition-prediction.onrender.com/\

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Health-Condition-Prediction.git
```

Go to project directory

```bash
cd Health-Condition-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

- Deep Learning Model
- SHAP Explainability
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment
- Model Monitoring

---

# 👨‍💻 Author

**Aranav Mandani**

🎓 B.E. Artificial Intelligence & Machine Learning

📍 Ahmedabad, Gujarat, India

---

# 🔗 Connect With Me

💼 **LinkedIn**

https://www.linkedin.com/in/aranav-mandani-a1785431b/

🐙 **GitHub**

https://github.com/aranavmandani

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing Machine Learning projects!

---

**Thank you for visiting! 😊**

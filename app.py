
 #reshape numpy aray as we are predicting for one instance

import streamlit as st
import numpy as np
import joblib  # Load the trained model

# Load the trained model (Ensure 'heart_disease_model.pkl' is in the same folder)
model = joblib.load("trained_model.sav")

# Streamlit UI
st.title("❤️ Heart Disease Prediction App")

# User Inputs
age = st.number_input("Age", min_value=20, max_value=100, value=20, step=1)

sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

cp = st.text_input("Chest Pain Type (CP)")

trestbps = st.slider("Resting Blood Pressure (Trestbps)", min_value=80, max_value=200, value=0)

chol = st.slider("Serum Cholesterol (Chol)", min_value=100, max_value=600, value=0)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (FBS)", options=[0, 1],
                   format_func=lambda x: "No (0)" if x == 0 else "Yes (1)")

restecg = st.selectbox("Resting ECG Results (Restecg)", options=[0, 1, 2],
                       format_func=lambda x: ["Normal (0)", "ST-T Wave Abnormality (1)", "Left Ventricular Hypertrophy (2)"][x])

thalach = st.slider("Maximum Heart Rate Achieved (Thalach)", min_value=60, max_value=220, value=0)

exang = st.selectbox("Exercise-Induced Angina (Exang)", options=[0, 1],
                     format_func=lambda x: "No (0)" if x == 0 else "Yes (1)")

oldpeak = st.slider("ST Depression Induced by Exercise (Oldpeak)", min_value=0.0, max_value=6.0, step=0.1, value=1.0)

slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2],
                     format_func=lambda x: ["Upsloping (0)", "Flat (1)", "Downsloping (2)"][x])

ca = st.selectbox("Number of Major Vessels (CA)", options=[0, 1, 2, 3, 4])

thal = st.text_input("Thalassemia Type (Thal)")

# Prepare input for prediction




# Convert input to numeric and handle empty values
try:
    features = np.array([
        float(age) if age else 0,
        int(sex) if sex else 0,
        int(cp) if cp else 0,
        float(trestbps) if trestbps else 0,
        float(chol) if chol else 0,
        int(fbs) if fbs else 0,
        int(restecg) if restecg else 0,
        float(thalach) if thalach else 0,
        int(exang) if exang else 0,
        float(oldpeak) if oldpeak else 0,
        int(slope) if slope else 0,
        int(ca) if ca else 0,
        int(thal) if thal else 0
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("❌ High Risk! Please consult a doctor.")
    else:
        st.success("✅ Low Risk! You are less likely to have heart disease.")

except ValueError:
    st.error("⚠️ Please fill in all fields correctly!")


import matplotlib.pyplot as plt

risk_factors = ['Age', 'Cholesterol', 'Blood Pressure']
values = [age, chol, trestbps]

fig, ax = plt.subplots()
ax.bar(risk_factors, values, color=['blue', 'red', 'green'])
st.pyplot(fig)






with st.expander("🍏 Calorie Counter & Diet for Heart Health"):
    st.markdown("<h2 class='sub-header'>Estimate Daily Calorie Needs</h2>", unsafe_allow_html=True)

    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    age_cal = st.number_input("Age", min_value=1, max_value=120, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

    # Calculate BMR (Basal Metabolic Rate)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age_cal + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age_cal - 161

    # Adjust for activity level
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }
    daily_calories = bmr * activity_multipliers[activity_level]

    st.write(f"🔹 Your estimated daily calorie requirement is **<span class='highlight'>{daily_calories:.0f} kcal</span>**.", unsafe_allow_html=True)











import streamlit as st

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .main-title {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            color: #b30000;
        }
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: #800000;
        }
        .highlight {
            color: #b30000;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='main-title'>🌍 Heart-Healthy Diet Chart ❤️</h1>", unsafe_allow_html=True)

# Country Selection
country = st.selectbox("🌎 Select Your Country", [
    "USA", "India", "UK", "China", "Italy", "Japan", "Mexico", "France", "Germany", "Brazil"
])

# Define Diet Plans
diet_plans = {
    "USA": {
        "Breakfast": ["Oatmeal with nuts & berries", "Whole grain toast with avocado", "Scrambled egg whites", "Green tea"],
        "Lunch": ["Grilled salmon with quinoa", "Steamed broccoli & carrots", "Lentil soup", "Olive oil-based salad"],
        "Dinner": ["Baked chicken breast", "Brown rice & steamed veggies", "Herbal tea"]
    },
    "India": {
        "Breakfast": ["Oats with almonds & banana", "Idli with sambar", "Green tea"],
        "Lunch": ["Brown rice with dal & sabzi", "Grilled paneer or chicken", "Curd with flaxseeds"],
        "Dinner": ["Multigrain roti with dal", "Steamed vegetables", "Turmeric milk"]
    },
    "UK": {
        "Breakfast": ["Porridge with honey & berries", "Whole wheat toast with peanut butter", "Black coffee"],
        "Lunch": ["Grilled fish with mashed sweet potatoes", "Steamed spinach", "Lentil soup"],
        "Dinner": ["Chicken stir-fry with quinoa", "Roasted brussels sprouts", "Herbal tea"]
    },
    "China": {
        "Breakfast": ["Brown rice porridge", "Steamed dumplings (veggie filling)", "Green tea"],
        "Lunch": ["Steamed fish with bok choy", "Brown rice & miso soup", "Tofu stir-fry"],
        "Dinner": ["Vegetable & tofu hotpot", "Steamed broccoli & carrots", "Jasmine tea"]
    },
    "Italy": {
        "Breakfast": ["Whole grain toast with olive oil", "Tomatoes & basil", "Espresso"],
        "Lunch": ["Grilled salmon with quinoa", "Steamed zucchini & eggplant", "Lentil soup"],
        "Dinner": ["Pasta (whole wheat) with tomato sauce", "Steamed vegetables", "Green tea"]
    },
    "Japan": {
        "Breakfast": ["Miso soup", "Steamed rice with nori", "Green tea"],
        "Lunch": ["Grilled fish with miso glaze", "Steamed spinach", "Brown rice"],
        "Dinner": ["Sushi (veggie & salmon)", "Miso soup", "Matcha tea"]
    },
    "Mexico": {
        "Breakfast": ["Whole wheat tortillas with beans", "Avocado & tomato slices", "Herbal tea"],
        "Lunch": ["Grilled chicken with brown rice", "Vegetable salsa", "Lentil soup"],
        "Dinner": ["Baked fish tacos", "Steamed broccoli", "Cinnamon tea"]
    },
    "France": {
        "Breakfast": ["Whole wheat croissant", "Fruit salad", "Black coffee"],
        "Lunch": ["Grilled salmon with ratatouille", "Lentil soup", "Olive oil-based salad"],
        "Dinner": ["Baked chicken with quinoa", "Steamed vegetables", "Herbal tea"]
    },
    "Germany": {
        "Breakfast": ["Rye bread with avocado", "Fruit smoothie", "Green tea"],
        "Lunch": ["Grilled chicken with sauerkraut", "Steamed potatoes", "Lentil soup"],
        "Dinner": ["Whole wheat pasta with tomato sauce", "Steamed spinach", "Herbal tea"]
    },
    "Brazil": {
        "Breakfast": ["Papaya with granola", "Whole wheat toast", "Black coffee"],
        "Lunch": ["Grilled fish with quinoa", "Steamed vegetables", "Black bean soup"],
        "Dinner": ["Baked chicken with brown rice", "Steamed broccoli", "Chimarrão tea"]
    }
}

# **Display Diet Plan in a Single Expander**
with st.expander("📋 **Diet Chart**", expanded=False):
    st.markdown(f"<h2 class='sub-header'>🍽️ Diet Plan for {country} </h2>", unsafe_allow_html=True)

    # **Breakfast**
    st.markdown("### 🥣 Breakfast")
    for item in diet_plans[country]["Breakfast"]:
        st.write(f"- ✅ {item}")

    # **Lunch**
    st.markdown("### 🍱 Lunch")
    for item in diet_plans[country]["Lunch"]:
        st.write(f"- ✅ {item}")

    # **Dinner**
    st.markdown("### 🍽️ Dinner")
    for item in diet_plans[country]["Dinner"]:
        st.write(f"- ✅ {item}")

st.success("💡 **Tip:** Eat fresh, avoid processed food, and stay hydrated! 🥗💧")

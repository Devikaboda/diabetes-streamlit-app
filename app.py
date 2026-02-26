
import joblib
import streamlit as st

st.title("Diabetes Prediction App")

try:
    model = joblib.load("trained_model.joblib")
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()   # stop app if model fails
st.write("Please enter the following details:")

preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The person is likely to have Diabetes")
    else:
        st.success("✅ The person is not likely to have Diabetes")

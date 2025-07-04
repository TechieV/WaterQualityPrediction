# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Inject custom CSS for Glass UI
st.markdown("""
    <style>
    .main {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        color: #fff;
    }
    body {
        background-image: linear-gradient(to right, #2c3e50, #3498db);
        color: white;
    }
    .css-18e3th9 {
        padding: 2rem 1rem 10rem;
    }
    .css-1d391kg {
        background: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model and structure
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# UI Title and Description
st.title("💧 Water Pollutants Predictor")
st.write("🌍 Predict the water pollutants based on Year and Station ID")

# User inputs
year_input = st.number_input("📅 Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("📍 Enter Station ID", value='1')

# Predict Button
if st.button('🚀 Predict'):
    if not station_id:
        st.warning('⚠️ Please enter the station ID')
    else:
        # Prepare the input
        input_df = pd.DataFrame({'year': [year_input], 'id':[station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align with model columns
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

        # Create a DataFrame for table output
        result_df = pd.DataFrame({
            'Pollutant': pollutants,
            'Predicted Level': [round(val, 2) for val in predicted_pollutants]
        })

        st.subheader(f"📊 Predicted pollutant levels for Station '{station_id}' in {year_input}:")
        st.dataframe(result_df, use_container_width=True)

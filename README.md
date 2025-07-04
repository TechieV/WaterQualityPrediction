# 💧 Water Pollutants Predictor

This project is a machine learning-based web application that predicts the levels of major water pollutants based on the **Year** and **Station ID**. It is built using **Streamlit** and trained on historical water quality data.

🔗 Live Demo: [https://waterqualitypredict.streamlit.app/](https://waterqualitypredict.streamlit.app/)

---

## 📊 Features

- Predict levels of pollutants: `O2`, `NO3`, `NO2`, `SO4`, `PO4`, `CL`
- Simple and intuitive web interface
- Built using Streamlit for fast deployment
- Accepts Year and Station ID as inputs
- Displays results in a clean, tabular format

---

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib / Pickle for model saving
- Streamlit for web app
- Gradient + Glassmorphism UI (custom CSS)

---

## 🗂️ Project Structure

.
├── app.py # Streamlit web app
├── WaterQuality.ipynb # Jupyter notebook for model training
├── pollution_model.pkl # Trained ML model (Joblib format)
├── model_columns.pkl # Model input columns (used for encoding)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

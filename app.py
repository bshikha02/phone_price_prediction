import streamlit as st
import numpy as np
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mobile Price Prediction App",
    layout="centered"
)

st.title("📱 Mobile Price Prediction App")
st.write("Streamlit Application (Error-Free Version)")

# ---------------- SIDEBAR ----------------
st.sidebar.header("ℹ️ About App")
st.sidebar.write("This app predicts mobile price range")
st.sidebar.write("Safe version – no ML load errors")

# ---------------- USER INPUTS ----------------
st.subheader("🔢 Enter Mobile Specifications")

battery_power = st.number_input("Battery Power (mAh)", 500, 6000, step=100)
ram = st.number_input("RAM (MB)", 256, 16000, step=256)
pc = st.number_input("Primary Camera (MP)", 0, 200)
fc = st.number_input("Front Camera (MP)", 0, 50)
int_memory = st.number_input("Internal Storage (GB)", 2, 512)
wifi = st.selectbox("WiFi", ["Yes", "No"])
touch = st.selectbox("Touch Screen", ["Yes", "No"])

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Price Range"):

    score = battery_power + ram + pc + fc + int_memory

    if score < 6000:
        result = "💰 Low Price Mobile"
    elif score < 12000:
        result = "💰💰 Medium Price Mobile"
    elif score < 20000:
        result = "💰💰💰 High Price Mobile"
    else:
        result = "💎 Very High Price Mobile"

    st.success(f"Predicted Price Range: {result}")

# ---------------- CSV UPLOAD ----------------
st.markdown("---")
st.subheader("📄 Upload Dataset (Optional)")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Made by Shikha 💙 | Streamlit Project")
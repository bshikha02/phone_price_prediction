import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    .main-title {
        font-size:40px;
        font-weight:bold;
        color:#4F46E5;
        text-align:center;
    }
    .card {
        background-color:#F3F4F6;
        padding:20px;
        border-radius:15px;
        text-align:center;
        font-size:18px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>📱 Mobile Price Prediction App</div>", unsafe_allow_html=True)
st.write("")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Prediction", "Dataset", "About"])

# ---------------- HOME ----------------
if menu == "Home":
    st.subheader("🏠 Welcome")
    st.write("""
    This is a **Mobile Price Prediction UI** built using **Streamlit**.
    
    👉 Clean UI  
    👉 Beginner Friendly  
    👉 Error Free  

    ML model can be added later.
    """)

# ---------------- PREDICTION UI ----------------
elif menu == "Prediction":
    st.subheader("🔮 Predict Mobile Price")

    col1, col2, col3 = st.columns(3)

    with col1:
        battery = st.slider("🔋 Battery (mAh)", 500, 6000, 3000)
        ram = st.slider("🧠 RAM (MB)", 256, 16000, 4000)

    with col2:
        pc = st.slider("📷 Primary Camera (MP)", 0, 200, 48)
        fc = st.slider("🤳 Front Camera (MP)", 0, 50, 16)

    with col3:
        storage = st.slider("💾 Storage (GB)", 4, 512, 64)
        wifi = st.selectbox("📡 WiFi", ["Yes", "No"])

    st.write("")
    if st.button("✨ Show Price Range"):
        score = battery + ram + pc + fc + storage

        if score < 6000:
            price = "Low Range 💰"
        elif score < 12000:
            price = "Medium Range 💰💰"
        elif score < 20000:
            price = "High Range 💰💰💰"
        else:
            price = "Premium 💎"

        st.markdown(f"<div class='card'>Predicted Price: <b>{price}</b></div>",
                    unsafe_allow_html=True)

# ---------------- DATASET ----------------
elif menu == "Dataset":
    st.subheader("📊 Dataset Preview")

    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df.head())

# ---------------- ABOUT ----------------
elif menu == "About":
    st.subheader("ℹ️ About Project")
    st.write("""
    **Project Title:** Mobile Price Prediction  
    **Technology:** Python, Streamlit  
    **Developed by:** Shikha  

    This project focuses on building a clean UI.
    Machine Learning integration can be done later.
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2026 | Streamlit UI Project")
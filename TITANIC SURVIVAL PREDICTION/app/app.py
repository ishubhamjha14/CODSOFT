import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from model import train_model

model, accuracy = train_model()

st.set_page_config(page_title="Titanic AI", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.block-container {
    padding-top: 2rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    color: white;
    font-weight: bold;
}

/* Card */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    padding: 40px;
    border-radius: 20px;
    width: 60%;
    margin: auto;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='title'>🚢 Titanic AI Predictor</div>", unsafe_allow_html=True)
st.write("")
st.markdown(f"<p style='text-align:center;color:white;'>Accuracy: {round(accuracy*100,2)}%</p>", unsafe_allow_html=True)

# ---------------- CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1,2,3])
    sex = st.selectbox("Gender", ["male","female"])
    age = st.slider("Age", 1, 80, 25)

with col2:
    sibsp = st.number_input("Siblings", 0, 5, 0)
    parch = st.number_input("Parents", 0, 5, 0)
    fare = st.number_input("Fare", 0.0, 500.0, 50.0)

embarked = st.selectbox("Embarked", ["C","Q","S"])

sex = 0 if sex == "male" else 1
embarked = {"C":0,"Q":1,"S":2}[embarked]

if st.button("🚀 Predict"):
    sample = [[pclass, sex, age, sibsp, parch, fare, embarked]]
    result = model.predict(sample)
    prob = model.predict_proba(sample)

    if result[0] == 1:
        st.success(f"Survival Chance: {round(prob[0][1]*100,2)}%")
    else:
        st.error(f"Survival Chance: {round(prob[0][1]*100,2)}%")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>Developed by Shubham Kumar Jha 🚀</div>", unsafe_allow_html=True)
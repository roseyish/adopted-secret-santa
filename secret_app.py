import streamlit as st
import random
import time

st.set_page_config(page_title="Secret Santa 🎄", page_icon="🎁", layout="centered")

names = ["Isha", "Dipsha", "Bhalla", "Anya"]

# ---------- GLOBAL RANDOM ASSIGNMENT ----------
@st.cache_data
def generate_assignments():
    while True:
        shuffled = random.sample(names, len(names))
        if all(names[i] != shuffled[i] for i in range(len(names))):
            return dict(zip(names, shuffled))

assignments = generate_assignments()

# ---------- UI ----------
st.markdown(
    "<h1 style='text-align:center; color:#c1121f;'>🎄 Secret Santa 🎄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Everyone can see everyone’s Secret Santa 🎁</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- DISPLAY ALL ----------
for giver, receiver in assignments.items():
    with st.container():
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #165b33, #1b4332);
                padding: 18px;
                border-radius: 15px;
                margin-bottom: 12px;
                font-size: 20px;
                color: white;
                box-shadow: 0 8px 20px rgba(0,0,0,0.35);
                display: flex;
                justify-content: space-between;
            ">
                <strong>{giver}</strong>
                <span>🎁 → <strong>{receiver}</strong></span>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br><center>✨ Merry Christmas & Happy Gifting ✨</center>", unsafe_allow_html=True)

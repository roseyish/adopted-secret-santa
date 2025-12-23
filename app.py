import streamlit as st
import random
import time

st.set_page_config(page_title="Secret Santa 🎄", page_icon="🎄", layout="centered")

names = ["Isha", "Yashika", "Bhalla", "Anya"]

# ---------- GLOBAL RANDOM ASSIGNMENT ----------
@st.cache_data
def generate_assignments():
    while True:
        shuffled = random.sample(names, len(names))
        if all(n != shuffled[i] for i, n in enumerate(names)):
            return dict(zip(names, shuffled))

assignments = generate_assignments()

# ---------- UI ----------
st.markdown(
    "<h1 style='text-align:center; color:#c1121f;'>🎄 Merry Christmas 🎄</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Choose your name to reveal your Secret Santa 🎁</p>",
    unsafe_allow_html=True
)

selected_name = st.selectbox("Who are you?", [""] + names)

if selected_name:
    st.markdown("---")
    with st.spinner("Shuffling gifts... 🎁"):
        time.sleep(1.5)

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #2a9d8f, #1b4332);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            font-size: 22px;
            color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            ">
            🎁 <br><br>
            You are gifting <br><br>
            <strong style="font-size:28px;">{assignments[selected_name]}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><center>✨ Made with Christmas spirit ✨</center>", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="Tori-Ana McNeil v20.26: Graduate Edition",
    page_icon="🎓",
    layout="centered"
)

# ---- GLOBAL STYLE ----
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(180deg, #F4F7F5 0%, #FFFFFF 100%);
}

/* Text */
html, body {
    color: #1C1C1C;
}

/* Hero */
.hero-title {
    text-align: center;
    font-size: 60px;
    font-weight: 700;
    color: #046A38;
    margin-bottom: 5px;
}

/* Gold accent */
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 15px auto 25px auto;
    border-radius: 5px;
}

/* Version text */
.version-text {
    text-align: center;
    font-family: monospace;
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
}

/* Terminal */
.terminal {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin: 20px auto;
    width: 80%;
}

/* Degree box */
.degree-box {
    text-align: center;
    background-color: #ffffff;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin: 20px auto;
    width: 80%;
}

/* Footer */
.footer-text {
    text-align: center;
    font-size: 16px;
    color: #555;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ---- Content ----
st.markdown('<div class="hero-title">System Update Complete</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="version-text">> Tori-Ana McNeil v20.26 successfully installed</div>', unsafe_allow_html=True)

st.markdown("""
<div class="terminal">
> initializing graduate.exe<br>
> loading credentials...<br>
> validating achievements...<br>
> status: SUCCESS ✔️
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="degree-box">
<b>B.S. in Data Science</b><br>
<b>B.S.B.A. in Management Information Systems</b><br>
<b>B.S.B.A. in Business Analytics</b><br>
Minor in Artificial Intelligence
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer-text">Scroll through the menu to explore deployment details 💚</div>', unsafe_allow_html=True)

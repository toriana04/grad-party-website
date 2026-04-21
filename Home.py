import streamlit as st

st.set_page_config(
    page_title="Tori-Ana McNeil v20.26: Graduate Edition",
    page_icon="🎓",
    layout="centered"
)

# ---- Styling ----
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #F8F9FA;
}

/* Hero Title */
.hero-title {
    text-align: center;
    font-size: 58px;
    font-weight: 700;
    color: #046A38;
    margin-bottom: 10px;
}

/* Subtitle */
.hero-subtitle {
    text-align: center;
    font-size: 20px;
    color: #1C1C1C;
    margin-bottom: 5px;
}

/* Version text (monospace = tech vibe) */
.version-text {
    text-align: center;
    font-family: monospace;
    font-size: 16px;
    color: #888;
    margin-bottom: 25px;
}

/* Degree block */
.degree-box {
    text-align: center;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin: 20px auto;
    width: 80%;
}

/* Footer text */
.footer-text {
    text-align: center;
    font-size: 16px;
    color: #555;
    margin-top: 30px;
}

/* Fake terminal */
.terminal {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin: 20px auto;
    width: 80%;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown('<div class="hero-title">System Update Complete</div>', unsafe_allow_html=True)

st.markdown('<div class="version-text">> Tori-Ana McNeil v20.26 successfully installed</div>', unsafe_allow_html=True)

# ---- Fake Terminal Boot ----
st.markdown("""
<div class="terminal">
> initializing graduate.exe<br>
> loading credentials...<br>
> validating achievements...<br>
> status: SUCCESS ✔️
</div>
""", unsafe_allow_html=True)

# ---- Degrees ----
st.markdown("""
<div class="degree-box">
<div class="hero-subtitle"><b>B.S. in Data Science</b></div>
<div class="hero-subtitle"><b>B.S.B.A. in Management Information Systems</b></div>
<div class="hero-subtitle"><b>B.S.B.A. in Business Analytics</b></div>
<div class="hero-subtitle">Minor in Artificial Intelligence</div>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown('<div class="footer-text">Scroll through the menu to explore deployment details 💚</div>', unsafe_allow_html=True)

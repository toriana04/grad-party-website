import streamlit as st

st.set_page_config(
    page_title="Tori-Ana McNeil v20.26: Graduate Edition",
    page_icon="🎓",
    layout="centered"
)

# ---- GLOBAL STYLE ----
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}
html, body, [class*="css"] {
    color: #FFFFFF;
}
.hero-title {
    text-align: center;
    font-size: 60px;
    font-weight: 700;
    color: #B9975B;
}
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 15px auto 25px auto;
    border-radius: 5px;
}
.version-text {
    text-align: center;
    font-family: monospace;
    color: #dcdcdc;
}
.terminal {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin: 20px auto;
    width: 80%;
}
.degree-box {
    text-align: center;
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    margin: 20px auto;
    width: 80%;
    color: #FFFFFF;   /* 👈 THIS FIXES IT */
}
.footer-text {
    text-align: center;
    color: #dcdcdc;
}
</style>
""", unsafe_allow_html=True)

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

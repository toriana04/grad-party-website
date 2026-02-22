import streamlit as st

st.set_page_config(
    page_title="Tori-Ana McNeil v22.26: Graduate Edition",
    page_icon="🎓",
    layout="centered"
)

# ---- Styling ----
st.markdown("""
<style>
body {
    background-color: #F8F9FA;
}
.hero-title {
    text-align: center;
    font-size: 52px;
    font-weight: 700;
    color: #046A38;
}
.hero-subtitle {
    text-align: center;
    font-size: 22px;
    color: #1C1C1C;
}
.centered {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown('<div class="hero-title">System Update Complete</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Tori- Ana McNeil v22.26 Successfully Installed</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">B.S. in Data Science</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">B.S.B.A. in Management Information Systems</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">B.S.B.A. in Business Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Minor in Artificial Intelligence</div>', unsafe_allow_html=True)
st.write("")

st.markdown('<div class="centered">Scroll through the menu to explore deployment details 💚</div>', unsafe_allow_html=True)
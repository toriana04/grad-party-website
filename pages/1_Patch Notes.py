import streamlit as st

st.set_page_config(page_title="Patch Notes", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}
html, body {
    color: white;
}
h1 {
    color: #B9975B;
    text-align: center;
}
.card {
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Patch Notes: Graduation v20.26</h1>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("""YOUR PARAGRAPH TEXT HERE (keep what you already wrote)""")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Current Status:")
st.progress(73)

st.markdown("Loading adulthood… ███████░░░ 73%")

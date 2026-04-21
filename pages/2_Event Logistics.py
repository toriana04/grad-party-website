import streamlit as st

st.set_page_config(page_title="Event Deployment", page_icon="📍")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}
html, body {
    color: white;
}
.section-title {
    color: #B9975B;
    font-size: 36px;
    font-weight: 700;
    text-align: center;
}
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 15px auto 30px auto;
}
.detail-box {
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}
.detail-title {
    color: #B9975B;
    font-weight: 600;
}
.note {
    text-align: center;
    color: #dcdcdc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Event Deployment</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="detail-box">
<div class="detail-title">🗓 Installation Date & Time</div>
May 17th, 2026<br>4 PM – 8 PM
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-box">
<div class="detail-title">📍 Deployment Location</div>
Berewick Manor House<br>
6625 Berewick Commons Pkwy<br>
Charlotte, NC 28278
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-box">
<div class="detail-title">👖 Appearance Settings</div>
Casual
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="detail-box">
<div class="detail-title">💚 Expected Output</div>
• Food & Refreshments<br>
• Music & Celebration<br>
• A whole lot of joy
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="note">Your presence is the greatest gift 💚</div>', unsafe_allow_html=True)

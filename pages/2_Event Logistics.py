import streamlit as st

st.set_page_config(page_title="Event Deployment", page_icon="📍")

# ---- Styling ----
st.markdown("""
<style>
.section-title {
    color: #046A38;
    font-size: 32px;
    font-weight: 600;
}
.detail-box {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}
.detail-title {
    font-size: 20px;
    font-weight: 600;
    color: #046A38;
}
.detail-text {
    font-size: 18px;
    color: #1C1C1C;
}
.note {
    font-size: 16px;
    color: #555555;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---- Page Title ----
st.markdown('<div class="section-title">Event Deployment</div>', unsafe_allow_html=True)
st.write("")

# ---- Date & Time ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">🗓 Installation Date & Time</div>
<div class="detail-text">
May 17th, 2026<br>
4 PM – 8 PM
</div>
</div>
""", unsafe_allow_html=True)

# ---- Location ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">📍 Deployment Location</div>
<div class="detail-text">
Berewick Manor House<br>
6625 Berewick Commons Pkway<br>
Charlotte, NC 28278
</div>
</div>
""", unsafe_allow_html=True)

# ---- Dress Code ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">👖 Appearance Settings</div>
<div class="detail-text">
Casual
</div>
</div>
""", unsafe_allow_html=True)

# ---- Additional Info ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">💚 What to Expect</div>
<div class="detail-text">
• Food & Refreshments<br>
• Music & Celebration<br>
• A whole lot of joy
</div>
</div>
""", unsafe_allow_html=True)

# ---- Footer Note ----
st.markdown("""
<div class="note">
I cannot wait to celebrate this milestone with you.  
Your presence is the greatest gift!
</div>
""", unsafe_allow_html=True)

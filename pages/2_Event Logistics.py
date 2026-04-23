import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Event Deployment", page_icon="📍")

# ---- Sidebar Header ----
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>System Menu</h2>
    <p>> select module</p>
</div>
""", unsafe_allow_html=True)

# ---- Styling ----
st.markdown("""
<style>

/* ===== SIDEBAR GOLD ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #B9975B 0%, #d4b87a 100%);
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #013220 !important;
}

/* Move header to TOP */
.sidebar-header {
    position: absolute;
    top: 20px;
    width: 100%;
    text-align: center;
}

/* Push nav down */
section[data-testid="stSidebarNav"] {
    margin-top: 100px;
}

/* Sidebar links */
section[data-testid="stSidebar"] a {
    color: #013220 !important;
}

/* Active page */
section[data-testid="stSidebar"] a[aria-current="page"] {
    color: #046A38 !important;
    font-weight: 700;
}

/* Hover */
section[data-testid="stSidebar"] a:hover {
    color: #046A38 !important;
}

/* ===== MAIN BACKGROUND ===== */
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}

/* Text */
html, body {
    color: white;
}

/* Title */
.section-title {
    color: #B9975B;
    font-size: 36px;
    font-weight: 700;
    text-align: center;
}

/* Divider */
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 15px auto 30px auto;
}

/* Cards */
.detail-box {
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    margin-bottom: 25px;
    color: #FFFFFF;
}

/* Card titles */
.detail-title {
    font-size: 20px;
    font-weight: 600;
    color: #B9975B;
}

/* Card text */
.detail-text {
    font-size: 18px;
    color: #FFFFFF;
}

/* Footer note */
.note {
    text-align: center;
    color: #dcdcdc;
}

</style>
""", unsafe_allow_html=True)

# ---- Page Title ----
st.markdown('<div class="section-title">Event Deployment</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---- Date & Time ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">🗓 Installation Date & Time</div>
<div class="detail-text">
May 17th, 2026<br>4 PM – 8 PM
</div>
</div>
""", unsafe_allow_html=True)

# ---- Location ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">📍 Deployment Location</div>
<div class="detail-text">
Berewick Manor House<br>
6625 Berewick Commons Pkwy<br>
Charlotte, NC 28278
</div>
</div>
""", unsafe_allow_html=True)

# ---- Dress Code ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">👖 Appearance Settings</div>
<div class="detail-text">
Snappy Casual
</div>
</div>
""", unsafe_allow_html=True)

# ---- Additional Info ----
st.markdown("""
<div class="detail-box">
<div class="detail-title">💚 Expected Output</div>
<div class="detail-text">
• Food & Refreshments<br>
• Music & Celebration<br>
• A whole lot of joy
</div>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown('<div class="note">Your presence is the greatest gift 💚</div>', unsafe_allow_html=True)

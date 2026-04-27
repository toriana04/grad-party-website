import streamlit as st

st.set_page_config(
    page_title="Tori-Ana McNeil v20.26: Graduate Edition",
    page_icon="🎓",
    layout="centered"
)

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

/* TEXT */
html, body, [class*="css"] {
    color: #FFFFFF;
}

/* HERO TITLE */
.hero-title {
    text-align: center;
    font-size: 60px;
    font-weight: 700;
    color: #B9975B;
}

/* DIVIDER */
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 15px auto 25px auto;
    border-radius: 5px;
}

/* VERSION TEXT */
.version-text {
    text-align: center;
    font-family: monospace;
    color: #dcdcdc;
}

/* TERMINAL */
.terminal {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin: 20px auto;
    width: 80%;
}

/* NAVIGATION BOX (replacing degree box) */
.degree-box {
    text-align: center;
    background-color: rgba(11, 61, 46, 0.7);
    padding: 25px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    margin: 20px auto;
    width: 80%;
    color: #FFFFFF;
}

/* FOOTER */
.footer-text {
    text-align: center;
    color: #dcdcdc;
}

</style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown('<div class="hero-title">System Update Complete</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="version-text">> Tori-Ana McNeil v20.26 successfully installed</div>', unsafe_allow_html=True)

# ---- Terminal ----
st.markdown("""
<div class="terminal">
> initializing graduate.exe<br>
> loading credentials...<br>
> validating achievements...<br>
> status: SUCCESS ✔️
</div>
""", unsafe_allow_html=True)

# ---- System Navigation ----
st.markdown("""
<div class="degree-box">
<h3 style='margin-bottom:10px;'>SYSTEM NAVIGATION</h3>

<p style='line-height:1.6;'>
Use the menu to explore the system:
</p>

<p style='line-height:1.8;'>
📍 <b>Celebration Details</b> — view event time, location, and vibes<br>
💌 <b>RSVP Protocol</b> — confirm your attendance
</p>

<p style='margin-top:15px; font-size:14px; opacity:0.7;'>
P.S. This entire site was built by me 💅🏽
</p>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown('<div class="footer-text">Navigate the system to access event details and RSVP 💚</div>', unsafe_allow_html=True)

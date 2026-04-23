import streamlit as st
from supabase import create_client

# ---- Page Config ----
st.set_page_config(page_title="RSVP Protocol", page_icon="💌")

# ---- Connect to Supabase ----
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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

/* ===== MAIN BACKGROUND ===== */
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}

/* TEXT */
html, body, label, span, p {
    color: #FFFFFF !important;
}

/* HEADERS */
h1, h2, h3 {
    color: #B9975B !important;
    text-align: center;
}

/* DIVIDER */
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 10px auto 20px auto;
}

/* FORM */
div[data-testid="stForm"] {
    background-color: #0B3D2E;
    padding: 30px;
    border-radius: 14px;
}

/* INPUTS */
input, textarea, select {
    background-color: #013220 !important;
    color: #FFFFFF !important;
    border: 1px solid #B9975B !important;
}

/* ===== BUTTON (FINAL FIX) ===== */
div[data-testid="stFormSubmitButton"] {
    width: 250%;
}

/* Button styling */
div[data-testid="stFormSubmitButton"] button {
    width: 250% !important;
    height: 60px;

    background-color: #B9975B !important;
    color: #046A38 !important;

    font-size: 20px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px;

    border-radius: 10px !important;
    border: none !important;

    white-space: nowrap;
}

/* Force inner text */
div[data-testid="stFormSubmitButton"] button * {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #046A38 !important;
}

/* Hover */
div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #d4b87a !important;
    color: #013220 !important;
}

/* TERMINAL */
.terminal-box {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
}

/* SUCCESS */
.success-box {
    background-color: #0B3D2E;
    color: #B9975B !important;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---- Headers ----
st.markdown('<h3>Guest Configuration</h3>', unsafe_allow_html=True)
st.markdown('<h1>Initialize RSVP Protocol</h1>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---- Terminal ----
st.markdown("""
<div class="terminal-box">
> system.boot()<br>
> loading event: Graduation_v20.26<br>
> verifying guest access...<br>
> status: ready ✔️
</div>
""", unsafe_allow_html=True)

# ---- Form ----
with st.form("guest_form"):

    name = st.text_input("User Identification (Name)")

    attending = st.radio(
        "Attendance Status",
        ["Yes 🎉 I will attend", "No 💌 Sending support remotely"]
    )

    guest_count = st.selectbox(
        "Total Party Size (including yourself)",
        list(range(1, 16))
    )

    message = st.text_area("Optional Message to Graduate")

    submitted = st.form_submit_button("Initialize My Response")

    if submitted:
        supabase.table("guest_configurations").insert({
            "name": name,
            "attendance": attending,
            "guest_count": guest_count,
            "message": message
        }).execute()

        st.markdown(
            '<div class="success-box">Response successfully deployed 💚 Thank you!</div>',
            unsafe_allow_html=True
        )

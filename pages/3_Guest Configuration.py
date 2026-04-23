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
<h2 style='text-align:center;'>System Menu</h2>
<p style='text-align:center; font-family:monospace;'>> select module</p>
""", unsafe_allow_html=True)

# ---- Styling ----
st.markdown("""
<style>

/* ===== SIDEBAR GOLD THEME ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #B9975B 0%, #d4b87a 100%);
}

/* Sidebar text = dark green */
section[data-testid="stSidebar"] * {
    color: #013220 !important;
}

/* Sidebar headers */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #013220 !important;
}

/* Sidebar links */
section[data-testid="stSidebar"] a {
    color: #013220 !important;
    font-weight: 500;
}

/* Hover */
section[data-testid="stSidebar"] a:hover {
    color: #046A38 !important;
}

/* Active page */
section[data-testid="stSidebar"] a[aria-current="page"] {
    color: #046A38 !important;
    font-weight: 700;
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

/* BUTTON */
div[data-testid="stFormSubmitButton"] {
    display: flex;
    justify-content: center;
}

div[data-testid="stFormSubmitButton"] button {
    background-color: #B9975B !important;
    color: #046A38 !important;
    font-weight: 700 !important;
    border-radius: 8px !important;

    width: 70%;
    height: 55px;
    font-size: 18px;

    white-space: nowrap;
}

div[data-testid="stFormSubmitButton"] button * {
    color: #046A38 !important;
}

/* HOVER */
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

    submitted = st.form_submit_button("Deploy")

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

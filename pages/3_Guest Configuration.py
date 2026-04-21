import streamlit as st
from supabase import create_client

# ---- Page Config ----
st.set_page_config(page_title="RSVP Protocol", page_icon="💌")

# ---- Connect to Supabase ----
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---- Styling ----
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}

/* Base text */
html, body, label, span, p {
    color: #FFFFFF !important;
}

/* Headers */
h1, h2, h3 {
    color: #B9975B !important;
    text-align: center;
}

/* Divider */
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 10px auto 20px auto;
    border-radius: 5px;
}

/* Form container */
div[data-testid="stForm"] {
    background-color: #0B3D2E;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
}

/* Inputs */
input, textarea, select {
    background-color: #013220 !important;
    color: #FFFFFF !important;
    border: 1px solid #B9975B !important;
    border-radius: 8px !important;
}

/* BUTTON FIX (THIS IS THE KEY PART) */
button[kind="primary"] {
    background-color: #B9975B !important;
    color: #046A38 !important;   /* green text */
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
}

/* Ensure inner text also green */
button[kind="primary"] * {
    color: #046A38 !important;
}

/* Hover */
button[kind="primary"]:hover {
    background-color: #d4b87a !important;
    color: #013220 !important;
}

/* Terminal box */
.terminal-box {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 25px;
    font-size: 14px;
}

/* SUCCESS MESSAGE FIX */
.success-box {
    background-color: #0B3D2E;
    color: #B9975B !important;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-top: 20px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---- Headers ----
st.markdown('<h3>Guest Configuration</h3>', unsafe_allow_html=True)
st.markdown('<h1>Initialize RSVP Protocol</h1>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---- Terminal Intro ----
st.markdown("""
<div class="terminal-box">
> system.boot()<br>
> loading event: Graduation_v20.26<br>
> verifying guest access...<br>
> status: ready ✔️
</div>
""", unsafe_allow_html=True)

# ---- RSVP Form ----
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

    submitted = st.form_submit_button("Deploy Response")

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

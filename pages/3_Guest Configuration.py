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
.section-title {
    color: #046A38;
    font-size: 30px;
    font-weight: 600;
}

/* MAIN RSVP TITLE */
.rsvp-title {
    text-align: center;
    font-size: 44px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* TERMINAL SUBTEXT */
.terminal-text {
    text-align: center;
    font-family: monospace;
    font-size: 16px;
    color: #888;
    margin-bottom: 25px;
}

/* Form Styling */
div[data-testid="stForm"] {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

/* Button Glow */
button[kind="primary"] {
    background-color: #046A38 !important;
    color: white !important;
    border-radius: 8px !important;
    height: 45px;
    font-weight: 600;
}

button[kind="primary"]:hover {
    box-shadow: 0px 0px 10px rgba(4,106,56,0.4);
}

/* Success Message */
.success-box {
    font-size: 18px;
    color: #046A38;
    font-weight: 500;
    margin-top: 20px;
    text-align: center;
}

/* Fake terminal block */
.terminal-box {
    background-color: #0f1117;
    color: #00ff9c;
    font-family: monospace;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 25px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown('<div class="section-title">Guest Configuration</div>', unsafe_allow_html=True)

st.markdown('<div class="rsvp-title">Initialize RSVP Protocol</div>', unsafe_allow_html=True)

st.markdown('<div class="terminal-text">> awaiting user input...</div>', unsafe_allow_html=True)

# ---- Fake Terminal Intro ----
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

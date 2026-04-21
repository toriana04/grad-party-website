import streamlit as st
from supabase import create_client

st.set_page_config(page_title="RSVP Protocol", page_icon="💌")

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    font-weight: 600;
}
.rsvp-title {
    text-align: center;
    font-size: 44px;
    color: #B9975B;
}
.gold-divider {
    height: 3px;
    width: 80px;
    background-color: #B9975B;
    margin: 10px auto 20px auto;
}
div[data-testid="stForm"] {
    background-color: #0B3D2E;
    padding: 30px;
    border-radius: 14px;
}
button[kind="primary"] {
    background-color: #B9975B !important;
    color: #013220 !important;
}
.terminal-box {
    background-color: #0f1117;
    color: #00ff9c;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Guest Configuration</div>', unsafe_allow_html=True)
st.markdown('<div class="rsvp-title">Initialize RSVP Protocol</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="terminal-box">
> system.boot()<br>
> verifying guest access...<br>
> status: ready ✔️
</div>
""", unsafe_allow_html=True)

with st.form("guest_form"):
    name = st.text_input("User Identification (Name)")
    attending = st.radio("Attendance Status", ["Yes 🎉", "No 💌"])
    guest_count = st.selectbox("Total Party Size", list(range(1, 16)))
    message = st.text_area("Optional Message")

    submitted = st.form_submit_button("Deploy Response")

    if submitted:
        supabase.table("guest_configurations").insert({
            "name": name,
            "attendance": attending,
            "guest_count": guest_count,
            "message": message
        }).execute()

        st.success("Response successfully deployed 💚")

import streamlit as st
from supabase import create_client

# ---- Page Config ----
st.set_page_config(page_title="Guest Configuration", page_icon="💌")

# ---- Connect to Supabase ----
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---- Styling ----
st.markdown("""
<style>
.section-title {
    color: #046A38;
    font-size: 34px;
    font-weight: 600;
}
.subtext {
    font-size: 18px;
    color: #555555;
    margin-bottom: 20px;
}
.form-box {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
}
.success-box {
    font-size: 18px;
    color: #046A38;
    font-weight: 500;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---- Page Title ----
st.markdown('<div class="section-title">Guest Configuration</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Please confirm your attendance below 💚</div>', unsafe_allow_html=True)

# ---- RSVP Form ----
with st.form("guest_form"):

    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    name = st.text_input("Full Name")

    attending = st.radio(
        "Attendance Status",
        ["Yes 🎉 I’ll be there!", "No 💌 Sending love from afar"]
    )

    guest_count = st.selectbox(
        "Number of Guests (including yourself)",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    message = st.text_area("Leave a message for the graduate (optional)")

    submitted = st.form_submit_button("Submit Configuration")

    st.markdown('</div>', unsafe_allow_html=True)

    if submitted:

        # Insert into Supabase
        supabase.table("guest_configurations").insert({
            "name": name,
            "attendance": attending,
            "guest_count": guest_count,
            "message": message
        }).execute()

        st.markdown(
            '<div class="success-box">Configuration received successfully 💚 Thank you for responding!</div>',
            unsafe_allow_html=True
        )
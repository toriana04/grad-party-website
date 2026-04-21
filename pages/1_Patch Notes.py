import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Patch Notes: Graduation v20.26", layout="centered")

# ---- Styling ----
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(180deg, #013220 0%, #046A38 100%);
}

/* Text */
html, body {
    color: #FFFFFF;
}

/* Title */
h1 {
    color: #B9975B;
    text-align: center;
}

/* Content Card */
.content-box {
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    color: #FFFFFF;
    font-size: 18px;
    line-height: 1.7;
}

/* Progress Bar */
div[data-testid="stProgressBar"] > div > div {
    background-color: #B9975B;
}

/* Subtle text */
.subtle {
    color: #dcdcdc;
}

</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<h1>🎓 Patch Notes: Graduation v20.26</h1>", unsafe_allow_html=True)

# ---- Content ----
st.markdown('<div class="content-box">', unsafe_allow_html=True)

st.markdown("""
From an early age, Tori has always been drawn to computers, endlessly curious about how technology works and how it shapes the world around us. What started as simple exploration quickly turned into a full-blown passion, eventually pairing with a growing interest in finance and data-driven decision making. Somewhere along the way, “just messing around with computers” evolved into a clear mission: to use technology and data to understand complex problems and build meaningful, real-world solutions.

Throughout her academic journey, Tori pursued this passion by earning a Bachelor of Science in Data Science, alongside a Bachelor of Science in Business Analytics and a Bachelor of Science in Management Information Systems, while also completing a minor in Artificial Intelligence. Yes, that is three degrees. No, she did not sleep. Her studies reflect a blend of technical skill, business strategy, and analytical thinking, allowing her to approach challenges from multiple angles at once. Graduating magna cum laude, she has demonstrated not only academic excellence, but also resilience, determination, and an impressive ability to survive on deadlines and determination alone.

Beyond the classroom, Tori gained hands-on experience through internships and projects focused on real-world applications of data and AI. She has built data-driven solutions, presented work to industry professionals, and developed a strong foundation in problem solving, communication, and innovation. Most notably, she designed and coded this entire website herself, because at this point, adding “full-stack developer for her own graduation” to the résumé felt appropriate.

This milestone represents more than the completion of multiple degrees. It marks the launch of a new chapter, one built on late nights, big ideas, and a slightly concerning number of open tabs. With a foundation in technology, a passion for finance, and a drive to make an impact, Tori is stepping forward ready to continue learning, building, and creating.

Graduation is not the end of the journey. It is simply the next version.
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---- Status Section ----
st.markdown("### Current Status:")
st.progress(73)

st.markdown("""
<div class="subtle">
Loading adulthood… ███████░░░ 73%<br>
<em>Estimated time remaining: unknown. System performance may vary.</em> 😌
</div>
""", unsafe_allow_html=True)

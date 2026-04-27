import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Patch Notes: Graduation v20.26", layout="centered")

# ---- Sidebar Header (NOW POSITIONED AT TOP) ----
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

/* Title */
h1 {
    color: #B9975B !important;
    text-align: center;
}

/* Content Card */
.content-box {
    background-color: #0B3D2E;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    color: #FFFFFF !important;
    font-size: 18px;
    line-height: 1.7;
}

/* Progress bar */
div[data-testid="stProgressBar"] > div > div {
    background-color: #B9975B;
}

/* Subtle text */
.subtle {
    color: #dcdcdc !important;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<h1>🎓 Patch Notes: Graduation v20.26</h1>", unsafe_allow_html=True)

# ---- Content ----
st.markdown("""
<div class="content-box">

From an early age, Tori-Ana has always been drawn to computers, endlessly curious about how technology works and how it shapes the world around us. What started as simple exploration quickly turned into a full-blown passion, eventually pairing with a growing interest in finance and data-driven decision making. Somewhere along the way, “just messing around with computers” evolved into a clear mission: to use technology and data to understand complex problems and build meaningful, real-world solutions.

<br><br>

Throughout her academic journey, Tori-Ana pursued this passion by earning a Bachelor of Science in Data Science, alongside a Bachelor of Science in Business Analytics and a Bachelor of Science in Management Information Systems, while also completing a minor in Artificial Intelligence. Yes, that is three degrees. No, she did not sleep. Her studies reflect a blend of technical skill, business strategy, and analytical thinking, allowing her to approach challenges from multiple angles at once. Graduating magna cum laude, she has demonstrated not only academic excellence, but also resilience, determination, and an impressive ability to survive on deadlines and determination alone.

<br><br>

Beyond the classroom, Tori-Ana gained hands-on experience through internships and projects focused on real-world applications of data and AI. She has built data-driven solutions, presented work to industry professionals, and developed a strong foundation in problem solving, communication, and innovation. Most notably, she designed and coded this entire website herself, because at this point, adding “full-stack developer for her own graduation” to the résumé felt appropriate.

<br><br>

This milestone represents more than the completion of multiple degrees. It marks the launch of a new chapter, one built on late nights, big ideas, and a slightly concerning number of open tabs. With a foundation in technology, a passion for finance, and a drive to make an impact, Tori-Ana is stepping forward ready to continue learning, building, and creating.

<br><br>

Graduation is not the end of the journey. It is simply the next version.

</div>
""", unsafe_allow_html=True)

# ---- Status ----
st.markdown('<h3 style="color:#B9975B; text-align:center;">Current Status:</h3>', unsafe_allow_html=True)
st.progress(73)

st.markdown("""
<div class="subtle">
Loading adulthood… ███████░░░ 73%<br>
<em>Estimated time remaining: unknown. System performance may vary.</em> 😌
</div>
""", unsafe_allow_html=True)

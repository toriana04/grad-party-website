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

# ---- Content (UPDATED STORY) ----
st.markdown("""
<div class="content-box">

My interest in technology started with me spending hours on the computer playing games, and it grew when my dad showed me how everything connected behind the scenes. From there, I started taking computer classes in middle school and added business courses in high school, where I became interested in how technology, data, and decision making all work together.

<br><br>

During high school, I earned a certificate in Information Technology from Central Piedmont Community College, which gave me a strong start and confirmed that this was the path I wanted to pursue. As a first generation college student, this journey has meant a lot, and it pushed me to figure things out, stay consistent, and keep going even when things were challenging.

<br><br>

In college, I pursued degrees in Business Analytics, Management Information Systems, and Data Science, and added a minor in Artificial Intelligence my senior year. Along the way, I developed a variety of projects, attended conferences, presented my work to professionals, and completed internships that helped me apply what I was learning in real-world settings. This website is one of those projects and reflects both my technical skills and creativity.

<br><br>

I will be graduating magna cum laude on May 8, 2026, and I am proud of everything this journey represents. This is just the beginning.

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

import streamlit as st

st.set_page_config(page_title="Patch Notes", page_icon="👩🏽‍🎓")

# ---- Styling ----
st.markdown("""
<style>
.section-title {
    color: #046A38;
    font-size: 32px;
    font-weight: 600;
}
.text-block {
    font-size: 18px;
    line-height: 1.7;
}
.highlight {
    color: #B9975B;
    font-weight: 600;
}
.dedication {
    font-style: italic;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---- Page Title ----
st.markdown('<div class="section-title">Graduate Patch Notes</div>', unsafe_allow_html=True)
st.write("")

# ---- Main Story ----
st.markdown("""
<div class="text-block">
Tori-Ana’s journey into technology began long before college.

Growing up, she was introduced to computers by her father. Watching him work, build, 
and speak passionately about technology sparked a deep curiosity. He not only showed 
her how computers worked, but also what was possible through innovation, 
entrepreneurship, and determination.

Listening to him talk about pursuing his own companies and navigating the corporate world 
inspired her to see technology not just as a skill but as a pathway to impact.

As that curiosity grew, so did her love for problem-solving, analytics, and understanding how 
data shapes the world around us. That passion eventually led her to pursue a degree in 
<span class="highlight">Data Science</span>, along with dual business degrees in 
<span class="highlight">Management Information Systems</span> and 
<span class="highlight">Business Analytics</span>, and a minor in 
<span class="highlight">Artificial Intelligence</span>.

This milestone is not just the completion of academic programs — it is the continuation 
of a foundation built at home, rooted in mentorship, ambition, and belief.
</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

# ---- Dedication Section ----
st.markdown("""
<div class="text-block dedication">
Special acknowledgment to the man who first opened the computer and showed me what was possible.
</div>
""", unsafe_allow_html=True)

st.write("")

st.divider()

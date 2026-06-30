"""
app.py

AI Recruiter Assistant
"""

import streamlit as st

from src.preprocess import (
    load_candidates,
    candidate_file
)

from src.jd_parser import read_job_description

from src.jd_analyzer import analyze_job_description

from src.ranking_engine import rank_candidates


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(

    page_title="AI Recruiter Assistant",

    page_icon="🤖",

    layout="wide"

)

# ----------------------------------------------------
# Title
# ----------------------------------------------------

st.title("🤖 AI Recruiter Assistant")

st.markdown(
    "### Intelligent Candidate Discovery & Ranking"
)

st.divider()

# ----------------------------------------------------
# Upload Section
# ----------------------------------------------------

left, right = st.columns([1, 2])

with left:

    st.subheader("📄 Upload Job Description")

    uploaded_file = st.file_uploader(

        "Upload DOCX",

        type=["docx"]

    )

    analyze_button = st.button(

        "🔍 Analyze Candidates",

        use_container_width=True

    )

# ----------------------------------------------------
# Wait Until Uploaded
# ----------------------------------------------------

if uploaded_file is None:

    with right:

        st.info(
            "Upload a Job Description to begin."
        )

    st.stop()

if not analyze_button:

    st.stop()

# ----------------------------------------------------
# Read JD
# ----------------------------------------------------

with st.spinner(

    "Reading Job Description..."

):

    job_text = read_job_description(

        uploaded_file

    )

# ----------------------------------------------------
# Analyze JD
# ----------------------------------------------------

with st.spinner(

    "Analyzing Job Description..."

):

    job_info = analyze_job_description(

        job_text

    )

# ----------------------------------------------------
# Load Candidates
# ----------------------------------------------------

with st.spinner(

    "Loading Candidates..."

):

    candidates = load_candidates(

        candidate_file

    )

# ----------------------------------------------------
# Ranking
# ----------------------------------------------------

with st.spinner(

    "Running AI Ranking Engine..."

):

    ranked_candidates = rank_candidates(

        candidates,

        job_text,

        job_info

    )

st.success(

    f"Successfully Ranked {len(ranked_candidates)} Candidates"

)

# ----------------------------------------------------
# Job Analysis
# ----------------------------------------------------

with left:

    st.divider()

    st.subheader("📊 Job Analysis")

    st.write(

        f"**Role :** {job_info['role']}"

    )

    st.write(

        f"**Experience :** {job_info['experience']}"

    )

    st.write(

        f"**Location :** {job_info['location']}"

    )

    st.write("**Required Skills**")

    if len(job_info["skills"]) == 0:

        st.warning(

            "No Skills Detected."

        )

    else:

        for skill in job_info["skills"]:

            st.write(f"✅ {skill}")
# ----------------------------------------------------
# Top Ranked Candidates
# ----------------------------------------------------

with right:

    st.subheader("🏆 Top Ranked Candidates")

    table = []

    top_candidates = ranked_candidates[:10]

    for rank, result in enumerate(top_candidates, start=1):

        table.append({

            "Rank": rank,

            "Candidate ID": result["candidate_id"],

            "Headline": result["headline"],

            "Final Score": round(
                result["final_score"],
                4
            )

        })

    st.dataframe(

        table,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

# ----------------------------------------------------
# Candidate Selector
# ----------------------------------------------------

candidate_options = []

for index, result in enumerate(top_candidates, start=1):

    candidate_options.append(

        f"Rank {index} | {result['candidate_id']}"

    )

selected_candidate = st.selectbox(

    "Select Candidate",

    candidate_options

)

selected_index = candidate_options.index(

    selected_candidate

)

result = top_candidates[selected_index]

candidate = result["candidate"]

# ----------------------------------------------------
# AI Score Cards
# ----------------------------------------------------

st.divider()

st.subheader("📈 AI Score Breakdown")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(

        "Semantic",

        round(

            result["semantic_score"],

            3

        )

    )

    st.metric(

        "Experience",

        round(

            result["experience_score"],

            3

        )

    )

with c2:

    st.metric(

        "Skill",

        round(

            result["skill_score"],

            3

        )

    )

    st.metric(

        "Behaviour",

        round(

            result["behaviour_score"],

            3

        )

    )

with c3:

    st.metric(

        "Semantic Skill",

        round(

            result["semantic_skill_score"],

            3

        )

    )

    st.metric(

        "Final Score",

        round(

            result["final_score"],

            3

        )

    )

st.divider()
# ----------------------------------------------------
# Candidate Profile
# ----------------------------------------------------

st.subheader("👤 Candidate Profile")

profile = candidate["profile"]

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Experience",
        f"{profile.get('years_of_experience', 0)} Years"
    )

    st.metric(
        "Current Company",
        profile.get("current_company", "-")
    )

with col2:

    st.metric(
        "Current Role",
        profile.get("current_title", "-")
    )

    st.metric(
        "Location",
        profile.get("location", "-")
    )

st.markdown("### Professional Summary")

st.write(
    profile.get("summary", "No summary available.")
)

# ----------------------------------------------------
# Skills
# ----------------------------------------------------

st.markdown("### 🛠 Technical Skills")

skills = []

for skill in candidate.get("skills", []):

    name = skill.get("name", "")

    if name:

        skills.append(name)

if len(skills) == 0:

    st.info("No Skills Available")

else:

    st.write(", ".join(skills))

# ----------------------------------------------------
# Career History
# ----------------------------------------------------

st.markdown("### 💼 Career History")

career = candidate.get("career_history", [])

if len(career) == 0:

    st.info("No Career History")

else:

    for job in career:

        with st.expander(

            f"{job.get('title','')} | {job.get('company','')}"

        ):

            st.write(

                f"Industry : {job.get('industry','-')}"

            )

            st.write(

                f"Duration : {job.get('duration_months',0)} Months"

            )

            if job.get("description"):

                st.write(

                    job.get("description")

                )

# ----------------------------------------------------
# Education
# ----------------------------------------------------

st.markdown("### 🎓 Education")

education = candidate.get("education", [])

if len(education) == 0:

    st.info("No Education Found")

else:

    for edu in education:

        st.write(
            f"**{edu.get('institution','')}**"
        )

        st.write(
            f"{edu.get('degree','')} | {edu.get('field_of_study','')}"
        )

        st.write("---")

# ----------------------------------------------------
# AI Explanation
# ----------------------------------------------------

st.markdown("### 🧠 Candidate Strengths")

for reason in result["reasons"]:

    st.success(reason)

st.markdown("### ⚠ Areas of Improvement")

if len(result["missing"]) == 0:

    st.success("No Missing Skills")

else:

    for skill in result["missing"]:

        st.warning(skill)

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.divider()

st.caption(
    "AI Recruiter Assistant • Phase 9.5"
)
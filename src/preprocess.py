from pathlib import Path
import json

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data" / "raw"

candidate_file = DATA_DIR / "candidates.jsonl"


# -----------------------------
# Load Candidates
# -----------------------------
def load_candidates(file_path):

    candidates = []

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:
            candidate = json.loads(line)
            candidates.append(candidate)

    return candidates


# -----------------------------
# Convert Candidate to AI Readable Text
# -----------------------------
def extract_candidate_text(candidate):

    profile = candidate["profile"]

    headline = profile.get("headline", "")
    experience = profile.get("years_of_experience", "")
    company = profile.get("current_company", "")
    title = profile.get("current_title", "")
    location = profile.get("location", "")
    country = profile.get("country", "")
    summary = profile.get("summary", "")

    career_history = candidate.get("career_history", [])
    education = candidate.get("education", [])
    certifications = candidate.get("certifications", [])
    languages = candidate.get("languages", [])

    text = f"""
==============================
CANDIDATE PROFILE
==============================

Current Role:
{title}

Headline:
{headline}

Years of Experience:
{experience}

Current Company:
{company}

Location:
{location}, {country}

Professional Summary:
{summary}
"""

    # -----------------------------
    # Skills
    # -----------------------------
    skill_names = []

    for skill in candidate.get("skills", [])[:20]:
        skill_names.append(skill.get("name", ""))

    skills_text = ", ".join(skill_names)

    text += f"""

Technical Skills:
{skills_text}
"""

    # -----------------------------
    # Career History
    # -----------------------------
    text += "\n\nCareer History:\n"

    for job in career_history:

        text += f"""

Company: {job.get("company", "")}

Role: {job.get("title", "")}

Industry: {job.get("industry", "")}

Duration: {job.get("duration_months", "")} months

Description:
{job.get("description", "")}
"""

    # -----------------------------
    # Education
    # -----------------------------
    text += "\n\nEducation:\n"

    for edu in education:

        text += f"""

Institution: {edu.get("institution", "")}

Degree: {edu.get("degree", "")}

Field of Study: {edu.get("field_of_study", "")}

Grade: {edu.get("grade", "")}
"""

    # -----------------------------
    # Certifications
    # -----------------------------
    text += "\n\nCertifications:\n"

    for cert in certifications:

        if isinstance(cert, dict):
            text += f"- {cert.get('name', '')}\n"
        else:
            text += f"- {cert}\n"

    # -----------------------------
    # Languages
    # -----------------------------
    text += "\n\nLanguages:\n"

    for lang in languages:

        if isinstance(lang, dict):
            text += f"- {lang.get('language', '')}\n"
        else:
            text += f"- {lang}\n"

    return text
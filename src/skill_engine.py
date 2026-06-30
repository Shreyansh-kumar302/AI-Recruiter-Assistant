"""
skill_engine.py

Purpose:
    Calculates skill matching scores between
    candidate skills and job description skills.

Phase:
    7.4
"""

from src.embedding_engine import (
    create_embedding,
    calculate_similarity
)

from src.skill_embedding_cache import get_skill_embedding


# ---------------------------------------------------------
# Exact Skill Match
# ---------------------------------------------------------

def calculate_skill_score(candidate, required_skills):

    candidate_skills = []

    for skill in candidate.get("skills", []):

        name = skill.get("name", "").lower()

        if name != "":
            candidate_skills.append(name)

    if len(required_skills) == 0:
        return 0

    matched = 0

    for skill in required_skills:

        if skill.lower() in candidate_skills:

            matched += 1

    return matched / len(required_skills)


# ---------------------------------------------------------
# Semantic Skill Match
# ---------------------------------------------------------

def calculate_semantic_skill_score(candidate, required_skills):

    candidate_skills = []

    for skill in candidate.get("skills", []):

        name = skill.get("name", "")

        if name != "":

            candidate_skills.append(name)

    # No skills available
    if len(candidate_skills) == 0 or len(required_skills) == 0:

        return 0

    # Candidate Skills
    candidate_text = ", ".join(candidate_skills)

    # JD Skills
    jd_text = ", ".join(required_skills)

    # Candidate Skill Embedding
    candidate_embedding = create_embedding(
        candidate_text
    )

    # Cached JD Skill Embedding
    jd_embedding = get_skill_embedding(
        jd_text
    )

    score = calculate_similarity(
        candidate_embedding,
        jd_embedding
    )

    return score
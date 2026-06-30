"""
reasoning_engine.py

Purpose:
    Generates explainable AI reasoning
    for candidate ranking.

Phase:
    8.4
"""


def generate_reason(candidate, job_info):

    strengths = []

    improvements = []

    # ---------------------------------------
    # Candidate Skills
    # ---------------------------------------

    candidate_skills = []

    for skill in candidate.get("skills", []):

        name = skill.get("name", "").lower()

        candidate_skills.append(name)

    matched = 0

    for skill in job_info["skills"]:

        if skill.lower() in candidate_skills:

            matched += 1

        else:

            improvements.append(
                f"{skill.title()} experience not found."
            )

    # ---------------------------------------
    # Skill Summary
    # ---------------------------------------

    if len(job_info["skills"]) > 0:

        ratio = matched / len(job_info["skills"])

        if ratio >= 0.80:

            strengths.append(
                "Strong match with the required technical skills."
            )

        elif ratio >= 0.50:

            strengths.append(
                "Matches a good portion of the required skills."
            )

        else:

            strengths.append(
                "Limited technical skill match."
            )

    # ---------------------------------------
    # Experience
    # ---------------------------------------

    candidate_exp = candidate["profile"].get(
        "years_of_experience",
        0
    )

    strengths.append(
        f"{candidate_exp} years of professional experience."
    )

    # ---------------------------------------
    # Behaviour
    # ---------------------------------------

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    if signals.get("open_to_work_flag"):

        strengths.append(
            "Actively open to new opportunities."
        )

    if signals.get(
        "recruiter_response_rate",
        0
    ) >= 0.70:

        strengths.append(
            "Excellent recruiter response rate."
        )

    elif signals.get(
        "recruiter_response_rate",
        0
    ) >= 0.40:

        strengths.append(
            "Good recruiter engagement."
        )

    if signals.get(
        "profile_completeness_score",
        0
    ) >= 90:

        strengths.append(
            "Highly complete professional profile."
        )

    if signals.get(
        "github_activity_score",
        0
    ) >= 8:

        strengths.append(
            "Strong GitHub activity."
        )

    if signals.get(
        "verified_email",
        False
    ):

        strengths.append(
            "Verified email address."
        )

    if signals.get(
        "verified_phone",
        False
    ):

        strengths.append(
            "Verified phone number."
        )

    return strengths, improvements
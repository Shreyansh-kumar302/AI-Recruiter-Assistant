"""
behaviour_engine.py

Purpose:
    Calculates recruiter behaviour score.

Phase:
    8.3
"""


def calculate_behaviour_score(candidate):

    signals = candidate.get("redrob_signals", {})

    score = 0.0

    # ---------------------------------------
    # Open To Work
    # ---------------------------------------

    if signals.get("open_to_work_flag", False):
        score += 0.15

    # ---------------------------------------
    # Recruiter Response Rate
    # ---------------------------------------

    recruiter_response = signals.get(
        "recruiter_response_rate",
        0
    )

    score += recruiter_response * 0.25

    # ---------------------------------------
    # Interview Completion Rate
    # ---------------------------------------

    interview_completion = signals.get(
        "interview_completion_rate",
        0
    )

    score += interview_completion * 0.20

    # ---------------------------------------
    # Offer Acceptance Rate
    # ---------------------------------------

    offer_acceptance = signals.get(
        "offer_acceptance_rate",
        0
    )

    score += offer_acceptance * 0.15

    # ---------------------------------------
    # Profile Completeness
    # ---------------------------------------

    profile = signals.get(
        "profile_completeness_score",
        0
    )

    score += (profile / 100) * 0.10

    # ---------------------------------------
    # GitHub Activity
    # ---------------------------------------

    github = signals.get(
        "github_activity_score",
        0
    )

    score += (github / 10) * 0.10

    # ---------------------------------------
    # Verified Email
    # ---------------------------------------

    if signals.get("verified_email", False):
        score += 0.025

    # ---------------------------------------
    # Verified Phone
    # ---------------------------------------

    if signals.get("verified_phone", False):
        score += 0.025

    return min(score, 1.0)
"""
experience_engine.py

Purpose:
    Calculates experience score between
    candidate experience and required experience.

Phase:
    8.2
"""

import re


def calculate_experience_score(candidate, job_info):

    candidate_exp = candidate["profile"].get(
        "years_of_experience",
        0
    )

    job_exp = job_info.get(
        "experience",
        ""
    )

    numbers = re.findall(r"\d+", job_exp)

    if len(numbers) == 0:
        return 1.0

    minimum_required = int(numbers[0])

    # ----------------------------------
    # Candidate has less experience
    # ----------------------------------

    if candidate_exp < minimum_required:

        return candidate_exp / minimum_required

    # ----------------------------------
    # Candidate satisfies requirement
    # ----------------------------------

    extra_years = candidate_exp - minimum_required

    bonus = extra_years * 0.02

    score = 1.0 + bonus

    return min(score, 1.10)
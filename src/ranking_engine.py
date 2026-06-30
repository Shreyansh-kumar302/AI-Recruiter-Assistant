"""
ranking_engine.py

Purpose:
    Combines all AI engines and ranks candidates.

Phase:
    7.3
"""

from src.preprocess import extract_candidate_text

from src.embedding_engine import create_embedding

from src.semantic_engine import calculate_semantic_score

from src.skill_engine import (
    calculate_skill_score,
    calculate_semantic_skill_score
)

from src.experience_engine import calculate_experience_score

from src.behaviour_engine import calculate_behaviour_score

from src.reasoning_engine import generate_reason


def rank_candidates(candidates, job_text, job_info):

    results = []

    required_skills = job_info["skills"]

    # ---------------------------------------
    # Create Job Embedding Only Once
    # ---------------------------------------

    job_embedding = create_embedding(job_text)

    # ---------------------------------------
    # Testing: First 100 Candidates
    # ---------------------------------------

    for candidate in candidates[:100]:

        # ---------------------------------------
        # Resume Text
        # ---------------------------------------

        candidate_text = extract_candidate_text(candidate)

        # ---------------------------------------
        # Semantic Score
        # ---------------------------------------

        semantic_score = calculate_semantic_score(
            candidate,
            candidate_text,
            job_embedding
        )

        # ---------------------------------------
        # Exact Skill Score
        # ---------------------------------------

        skill_score = calculate_skill_score(
            candidate,
            required_skills
        )

        # ---------------------------------------
        # Semantic Skill Score
        # ---------------------------------------

        semantic_skill_score = calculate_semantic_skill_score(
            candidate,
            required_skills
        )

        # ---------------------------------------
        # Experience Score
        # ---------------------------------------

        experience_score = calculate_experience_score(
            candidate,
            job_info
        )

        # ---------------------------------------
        # Behaviour Score
        # ---------------------------------------

        behaviour_score = calculate_behaviour_score(
            candidate
        )

        # ---------------------------------------
        # Explainability
        # ---------------------------------------

        reasons, missing = generate_reason(
            candidate,
            job_info
        )

        # ---------------------------------------
        # Combined Skill Score
        # ---------------------------------------

        combined_skill_score = (
            0.40 * skill_score +
            0.60 * semantic_skill_score
        )

        # ---------------------------------------
        # Final Hybrid Score
        # ---------------------------------------

        final_score = (
            0.40 * semantic_score +
            0.25 * combined_skill_score +
            0.20 * experience_score +
            0.15 * behaviour_score
        )

        # ---------------------------------------
        # Save Result
        # ---------------------------------------

        results.append({

            "candidate_id": candidate["candidate_id"],

            "headline": candidate["profile"].get(
                "headline",
                ""
            ),

            "semantic_score": semantic_score,

            "skill_score": skill_score,

            "semantic_skill_score": semantic_skill_score,

            "experience_score": experience_score,

            "behaviour_score": behaviour_score,

            "final_score": final_score,

            "reasons": reasons,

            "missing": missing,

            "candidate": candidate

        })

    # ---------------------------------------
    # Sort by Final Score
    # ---------------------------------------

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results
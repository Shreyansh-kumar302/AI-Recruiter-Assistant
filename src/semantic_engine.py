

from src.embedding_engine import (
    calculate_similarity
)

from src.embedding_cache import get_cached_embedding


def calculate_semantic_score(
    candidate,
    candidate_text,
    job_embedding
):

    candidate_id = candidate["candidate_id"]

    candidate_embedding = get_cached_embedding(
        candidate_id,
        candidate_text
    )

    score = calculate_similarity(
        candidate_embedding,
        job_embedding
    )

    return score
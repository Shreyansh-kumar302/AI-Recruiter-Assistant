"""
skill_embedding_cache.py

Purpose:
    Cache Job Skill Embeddings.

Phase:
    7.4
"""

from src.embedding_engine import create_embedding

_cached_skill_embeddings = {}


def get_skill_embedding(skill_text):

    if skill_text in _cached_skill_embeddings:

        return _cached_skill_embeddings[skill_text]

    embedding = create_embedding(skill_text)

    _cached_skill_embeddings[skill_text] = embedding

    return embedding
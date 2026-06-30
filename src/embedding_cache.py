

from pathlib import Path
import numpy as np

from src.embedding_engine import create_embedding


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CACHE_DIR = PROJECT_ROOT / "output" / "embeddings"

CACHE_DIR.mkdir(parents=True, exist_ok=True)


def get_cached_embedding(candidate_id, text):

    cache_file = CACHE_DIR / f"{candidate_id}.npy"

    # ----------------------------
    # Already Exists
    # ----------------------------

    if cache_file.exists():

        return np.load(cache_file)

    # ----------------------------
    # Create New Embedding
    # ----------------------------

    embedding = create_embedding(text)

    np.save(cache_file, embedding)

    return embedding
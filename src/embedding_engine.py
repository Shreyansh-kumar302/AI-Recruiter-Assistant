from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):

    embedding = model.encode(text)

    return embedding


def calculate_similarity(candidate_embedding, job_embedding):

    score = cosine_similarity(
        [candidate_embedding],
        [job_embedding]
    )

    return score[0][0]
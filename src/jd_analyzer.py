import re


def analyze_job_description(job_text):

    job = {

        "skills": [],

        "experience": "",

        "location": "",

        "role": ""

    }

    lower_text = job_text.lower()

    # ---------------------------------------------------
    # Experience
    # ---------------------------------------------------

    exp = re.search(r"\d+\s*-\s*\d+\s*years", lower_text)

    if exp:

        job["experience"] = exp.group()

    # ---------------------------------------------------
    # Role
    # ---------------------------------------------------

    first_line = job_text.split("\n")[0]

    if ":" in first_line:

        job["role"] = first_line.split(":")[-1].strip()

    # ---------------------------------------------------
    # Location
    # ---------------------------------------------------

    for line in job_text.split("\n"):

        if line.lower().startswith("location"):

            job["location"] = line.split(":")[-1].strip()

    # ---------------------------------------------------
    # Skill Alias Dictionary
    # ---------------------------------------------------

    skill_aliases = {

        "python": [
            "python",
            "python3"
        ],

        "sql": [
            "sql"
        ],

        "aws": [
            "aws",
            "amazon web services"
        ],

        "spark": [
            "spark"
        ],

        "airflow": [
            "airflow"
        ],

        "rag": [
            "rag",
            "retrieval augmented generation"
        ],

        "retrieval": [
            "retrieval"
        ],

        "llm": [
            "llm",
            "llms",
            "large language model",
            "large language models"
        ],

        "langchain": [
            "langchain"
        ],

        "vector database": [
            "vector database",
            "vector db",
            "pinecone",
            "milvus",
            "weaviate",
            "qdrant"
        ],

        "embedding": [
            "embedding",
            "embeddings"
        ],

        "fine-tuning": [
            "fine tuning",
            "fine-tuning"
        ],

        "machine learning": [
            "machine learning"
        ],

        "deep learning": [
            "deep learning"
        ],

        "docker": [
            "docker"
        ],

        "kubernetes": [
            "kubernetes"
        ],

        "pytorch": [
            "pytorch"
        ],

        "tensorflow": [
            "tensorflow"
        ]

    }

    # ---------------------------------------------------
    # Extract Skills
    # ---------------------------------------------------

    for skill, aliases in skill_aliases.items():

        for alias in aliases:

            if alias in lower_text:

                job["skills"].append(skill)

                break

    return job
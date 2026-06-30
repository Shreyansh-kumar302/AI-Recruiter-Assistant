"""
jd_parser.py

Purpose:
    Reads a Job Description from a DOCX file.

Phase:
    9.3
"""

from docx import Document


def read_job_description(file):

    doc = Document(file)

    paragraphs = []

    for paragraph in doc.paragraphs:

        text = paragraph.text.strip()

        if text:

            paragraphs.append(text)

    return "\n".join(paragraphs)
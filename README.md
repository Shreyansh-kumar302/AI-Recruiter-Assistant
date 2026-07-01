<div align="center">

# 🤖 AI Recruiter Assistant

### AI-Powered Candidate Discovery & Intelligent Resume Ranking Platform

<p>

An intelligent recruitment platform that leverages <b>Semantic Search</b>,
<b>Sentence Transformers</b>, <b>Explainable AI</b>, and
<b>Machine Learning</b> to automatically identify and rank the best candidates
for any Job Description.

</p>

<p>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)

![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-orange?style=for-the-badge&logo=pytorch)

![NLP](https://img.shields.io/badge/NLP-Semantic_Search-success?style=for-the-badge)

![GitHub](https://img.shields.io/badge/Open_Source-GitHub-black?style=for-the-badge&logo=github)

</p>

</div>

---

# 🚀 Project Overview

Hiring the right candidate has become increasingly challenging as recruiters receive hundreds or even thousands of resumes for a single position.

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which often overlooks highly qualified candidates whose resumes use different terminology.

**AI Recruiter Assistant** solves this challenge by combining modern Artificial Intelligence techniques with Explainable AI to identify candidates based on the semantic meaning of their profiles rather than exact keyword matches.

The platform analyzes both the Job Description and candidate profiles using Sentence Transformers, evaluates multiple ranking factors, and provides recruiters with transparent AI-generated recommendations through an interactive Streamlit dashboard.

---

# 🎯 Project Objectives

- Reduce manual resume screening effort.
- Improve candidate ranking accuracy using Semantic Search.
- Combine multiple AI scoring engines into one hybrid ranking model.
- Provide transparent AI-based explanations for every recommendation.
- Deliver an interactive recruiter-friendly dashboard.

---
# ✨ Key Features

### 📄 Smart Job Description Analysis

- Upload Job Description in **.docx** format.
- Automatic extraction of:
  - Job Role
  - Required Skills
  - Experience
  - Location

---

### 🤖 AI-Powered Candidate Ranking

Candidates are ranked using a hybrid AI ranking model that combines multiple evaluation engines instead of relying on simple keyword matching.

---

### 🧠 Semantic Resume Matching

Uses **Sentence Transformers (all-MiniLM-L6-v2)** to understand the semantic meaning of candidate profiles and job descriptions.

This enables the system to identify relevant candidates even when different terminology is used.

---

### 🎯 Technical Skill Matching

The platform evaluates:

- Exact Skill Matching
- Semantic Skill Matching

This produces significantly better results than traditional ATS systems.

---

### 💼 Experience Evaluation

Automatically compares candidate experience with job requirements and generates an experience score.

---

### 📊 Behaviour Intelligence

Candidate ranking also considers recruiter behaviour signals such as:

- Open to Work
- Recruiter Response Rate
- Interview Completion Rate
- Offer Acceptance Rate
- Profile Completeness
- GitHub Activity
- Verified Contact Information

---

### 📝 Explainable AI

Instead of providing only a score, the platform explains:

✅ Candidate Strengths

✅ Missing Skills

✅ Hiring Recommendations

making the AI decisions transparent for recruiters.

---

### 📈 Interactive Dashboard

Built using Streamlit.

Provides:

- Candidate Ranking Table
- AI Score Cards
- Candidate Profile
- Career History
- Education
- Skills
- AI Explanation

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home Page](assets/home.png)

---

## 🏆 Candidate Ranking

![Candidate Ranking](assets/ranking.png)

---

## 👤 Candidate Profile

![Candidate Profile](assets/profile.png)

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.11 |
| User Interface | Streamlit |
| Natural Language Processing | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Deep Learning | PyTorch |
| Machine Learning | Scikit-Learn |
| Data Processing | NumPy |
| Data Analysis | Pandas |
| Document Parsing | python-docx |
| Similarity Metric | Cosine Similarity |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 📦 Python Libraries

- streamlit
- sentence-transformers
- torch
- scikit-learn
- numpy
- pandas
- python-docx

---
# 🏗 System Architecture

```text
                         ┌──────────────────────────┐
                         │  Job Description (.docx) │
                         └─────────────┬────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │      JD Parser           │
                         └─────────────┬────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │     JD Analyzer          │
                         └─────────────┬────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │ Required Skill Extraction│
                         └─────────────┬────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │ Candidate Data Loader    │
                         └─────────────┬────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────┐
                    │       AI Ranking Engine            │
                    └────────────────────────────────────┘
                                       │
         ┌──────────────┬──────────────┼──────────────┬──────────────┐
         ▼              ▼              ▼              ▼              ▼
 ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
 │ Semantic   │  │ Skill      │  │ Experience │  │ Behaviour  │  │ Explainable│
 │ Engine     │  │ Engine     │  │ Engine     │  │ Engine     │  │ AI Engine  │
 └────────────┘  └────────────┘  └────────────┘  └────────────┘  └────────────┘
         └──────────────┬──────────────┬──────────────┘
                        ▼
               ┌───────────────────────┐
               │ Final Candidate Score │
               └─────────────┬─────────┘
                             ▼
               ┌───────────────────────┐
               │ Streamlit Dashboard   │
               └───────────────────────┘
```

---

# ⚙ AI Ranking Pipeline

The candidate ranking process follows the workflow below:

1. Recruiter uploads a Job Description.
2. The Job Description is parsed and analyzed.
3. Required skills, experience and location are extracted.
4. Candidate profiles are loaded from the dataset.
5. Resume embeddings are generated using Sentence Transformers.
6. Semantic similarity between the resume and Job Description is calculated.
7. Exact skill matching score is computed.
8. Semantic skill similarity score is calculated.
9. Experience score is generated.
10. Recruiter behaviour score is evaluated.
11. Explainable AI generates candidate strengths and missing skills.
12. All scores are combined into a hybrid ranking score.
13. Candidates are sorted in descending order.
14. Top candidates are displayed on the Streamlit dashboard.

---

# 🧠 AI Ranking Formula

The final ranking score is calculated using a weighted hybrid scoring model.

| Component | Weight |
|-----------|--------|
| Semantic Matching | **40%** |
| Skill Matching (Exact + Semantic) | **25%** |
| Experience Score | **20%** |
| Behaviour Score | **15%** |

---

## Final Score Formula

```text
Final Score

= (0.40 × Semantic Score)

+ (0.25 × Skill Score)

+ (0.20 × Experience Score)

+ (0.15 × Behaviour Score)
```

---

# 📊 AI Scoring Engines

## 🧠 Semantic Engine

Responsible for understanding the semantic meaning of candidate profiles using Sentence Transformers.

---

## 🎯 Skill Engine

Evaluates both:

- Exact Skill Matching
- Semantic Skill Matching

---

## 💼 Experience Engine

Measures candidate experience against job requirements and assigns an experience score.

---

## 📈 Behaviour Engine

Calculates recruiter behaviour signals including:

- Open to Work
- Recruiter Response Rate
- Interview Completion
- Offer Acceptance
- Profile Completeness
- GitHub Activity
- Verified Contact Information

---

## 📝 Explainable AI Engine

Provides transparent reasoning for every ranked candidate.

Outputs include:

- Candidate Strengths
- Missing Skills
- AI Hiring Recommendation

---

# 🔄 End-to-End Workflow

```text
Job Description

↓

JD Parsing

↓

JD Analysis

↓

Candidate Loading

↓

Embedding Generation

↓

Semantic Matching

↓

Skill Matching

↓

Experience Evaluation

↓

Behaviour Analysis

↓

Explainable AI

↓

Hybrid Score Calculation

↓

Candidate Ranking

↓

Recruiter Dashboard
```

---
# 📂 Project Structure

```text
AI-Recruiter-Assistant/

├── assets/
│   ├── home.png
│   ├── ranking.png
│   └── profile.png
│
├── data/
│   └── raw/
│       ├── candidate_schema.json
│       ├── candidates.jsonl
│       ├── job_description.docx
│       └── ...
│
├── output/
│   └── embeddings/
│
├── src/
│   ├── __init__.py
│   ├── behaviour_engine.py
│   ├── embedding_cache.py
│   ├── embedding_engine.py
│   ├── experience_engine.py
│   ├── jd_analyzer.py
│   ├── jd_parser.py
│   ├── preprocess.py
│   ├── ranking_engine.py
│   ├── reasoning_engine.py
│   ├── semantic_engine.py
│   ├── skill_embedding_cache.py
│   └── skill_engine.py
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Shreyansh-kumar302/AI-Recruiter-Assistant.git
```

---

## 2️⃣ Enter Project Directory

```bash
cd AI-Recruiter-Assistant
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Launch Application

```bash
streamlit run app.py
```

---

# ▶️ How to Use

## Step 1

Launch the Streamlit application.

---

## Step 2

Upload a Job Description in **.docx** format.

---

## Step 3

Click **Analyze Candidates**.

---

## Step 4

The platform automatically:

- Reads the Job Description
- Extracts role, experience and skills
- Loads candidate profiles
- Runs all AI scoring engines
- Generates candidate rankings

---

## Step 5

Explore:

- 🏆 Top Ranked Candidates
- 📈 AI Score Breakdown
- 👤 Candidate Profile
- 💼 Career History
- 🎓 Education
- 📝 Explainable AI Insights

---

# 🧪 Example Workflow

```text
Upload Job Description

↓

Analyze Job Requirements

↓

Load Candidate Dataset

↓

Generate Embeddings

↓

Run Semantic Matching

↓

Calculate Skill Score

↓

Calculate Experience Score

↓

Calculate Behaviour Score

↓

Generate Explainable AI

↓

Calculate Final Score

↓

Display Ranked Candidates
```

---

# 📁 Dataset Information

The application uses a structured candidate dataset containing:

- Candidate Profile
- Technical Skills
- Career History
- Education
- Certifications
- Languages
- Recruiter Behaviour Signals

The large dataset (`candidates.jsonl`) is intentionally excluded from this repository because it exceeds GitHub's file size limit. To run the application locally, place the dataset in:

```text
data/raw/candidates.jsonl
```

---

# ⚡ Performance Optimizations

The project includes multiple optimizations for faster execution:

- Embedding Caching
- Cached Skill Embeddings
- Single Job Embedding Generation
- Optimized Candidate Ranking Pipeline
- Efficient Cosine Similarity Computation

---

# 🧩 Core Modules

| Module | Responsibility |
|---------|----------------|
| `jd_parser.py` | Reads Job Description |
| `jd_analyzer.py` | Extracts role, skills, experience and location |
| `preprocess.py` | Loads candidate dataset |
| `embedding_engine.py` | Creates embeddings and similarity scores |
| `semantic_engine.py` | Semantic resume matching |
| `skill_engine.py` | Exact + semantic skill evaluation |
| `experience_engine.py` | Experience scoring |
| `behaviour_engine.py` | Recruiter behaviour scoring |
| `reasoning_engine.py` | Explainable AI insights |
| `ranking_engine.py` | Hybrid candidate ranking |

---
# 🌟 Project Highlights

- 🤖 AI-powered candidate ranking platform
- 🧠 Semantic Resume Matching using Sentence Transformers
- 🎯 Hybrid AI Scoring Model
- 📊 Explainable AI Recommendations
- 📄 Automated Job Description Analysis
- 📈 Interactive Streamlit Dashboard
- ⚡ Optimized Embedding Cache System
- 💼 Behaviour Intelligence Engine
- 🔍 Transparent Candidate Evaluation
- 🚀 Modular & Scalable Project Architecture

---

# 📌 Challenges Solved

During the development of this project, several real-world engineering challenges were addressed:

- Handling large candidate datasets efficiently.
- Reducing embedding generation time through caching.
- Combining multiple AI scoring engines into a unified ranking model.
- Improving semantic understanding beyond keyword matching.
- Making AI decisions transparent using Explainable AI.
- Building an interactive recruiter-friendly dashboard.

---



# 🤝 Team

This project was collaboratively developed by:

## 👨‍💻 Shreyansh Kumar

### Contributions

- AI Pipeline Design
- Semantic Search Engine
- Candidate Ranking Engine
- Explainable AI
- Streamlit Dashboard Integration
- GitHub Repository Management

GitHub:

https://github.com/Shreyansh-kumar302

---

## 👩‍💻 Aneesha Goswami

### Contributions

- Project Collaboration
- Testing & Validation
- Documentation Support

GitHub:

https://github.com/aneesha-04

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers behind the following technologies:

- Python
- Streamlit
- Sentence Transformers
- PyTorch
- Scikit-Learn
- NumPy
- Pandas
- Hugging Face

These libraries made this project possible.

---

# 📈 Project Status

| Status | Progress |
|----------|----------|
| Core AI Pipeline | ✅ Completed |
| Streamlit Dashboard | ✅ Completed |
| Semantic Ranking | ✅ Completed |
| Explainable AI | ✅ Completed |
| GitHub Documentation | ✅ Completed |
| UI Enhancements | 🚧 In Progress |
| Cloud Deployment | 📅 Planned |

---

# 📜 License

This repository is shared for educational and learning purposes.

Please provide appropriate attribution before reusing substantial portions of the code.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🛠 Suggest improvements
- 🐞 Report issues

Contributions and feedback are always welcome.

---

<div align="center">

### Thank you for visiting this repository ❤️

If you like this project, don't forget to ⭐ the repository.

</div>
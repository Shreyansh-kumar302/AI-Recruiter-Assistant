"""
main.py

Purpose:
    Main entry point of the AI Recruiter.

Phase:
    8.4
"""

from preprocess import load_candidates, candidate_file

from jd_parser import read_job_description, jd_file

from jd_analyzer import analyze_job_description

from ranking_engine import rank_candidates


# --------------------------------------------------------
# Candidate Profile Viewer
# --------------------------------------------------------

def print_candidate_profile(candidate):

    print("=" * 80)

    print(f"Candidate ID : {candidate['candidate_id']}")

    print(f"Headline     : {candidate['profile'].get('headline', '')}")

    print(f"Experience   : {candidate['profile'].get('years_of_experience', 0)} Years")

    print(f"Company      : {candidate['profile'].get('current_company', '')}")

    print(f"Role         : {candidate['profile'].get('current_title', '')}")

    print(f"Location     : {candidate['profile'].get('location', '')}")

    print("\nCareer History")

    for job in candidate.get("career_history", []):

        print(f"• {job.get('company', '')}")

        print(f"  Role : {job.get('title', '')}")

        print(f"  Duration : {job.get('duration_months', '')} months\n")

    print("Education")

    for edu in candidate.get("education", []):

        print(f"• {edu.get('institution', '')}")

        print(f"  Degree : {edu.get('degree', '')}")

        print()

    print("Top Skills")

    skills = []

    for skill in candidate.get("skills", [])[:10]:

        skills.append(skill.get("name", ""))

    print(", ".join(skills))

    print("=" * 80)


# --------------------------------------------------------
# Main
# --------------------------------------------------------

def main():

    print("\nLoading Candidates...\n")

    all_candidates = load_candidates(candidate_file)

    print(f"✓ Loaded {len(all_candidates)} Candidates")

    print("\nReading Job Description...\n")

    job_text = read_job_description(jd_file)

    print("✓ Job Description Loaded")

    print("\nAnalyzing Job Description...\n")

    job_info = analyze_job_description(job_text)

    print("✓ Job Analysis Complete")

    print("\n================ JOB ANALYSIS ================\n")

    print(f"Role       : {job_info['role']}")

    print(f"Experience : {job_info['experience']}")

    print(f"Location   : {job_info['location']}")

    print("\nRequired Skills")

    for skill in job_info["skills"]:

        print(f"• {skill}")

    print("\nRanking Candidates...\n")

    ranked_candidates = rank_candidates(
        all_candidates,
        job_text,
        job_info
    )

    print("✓ Ranking Complete")

    print("\n================ TOP 10 CANDIDATES ================\n")

    for rank, candidate in enumerate(ranked_candidates[:10], start=1):

        print("=" * 80)

        print(f"Rank #{rank}")

        print(f"Candidate ID         : {candidate['candidate_id']}")

        print(f"Headline             : {candidate['headline']}")

        print(f"Semantic Score       : {candidate['semantic_score']:.4f}")

        print(f"Skill Score          : {candidate['skill_score']:.4f}")

        print(f"Semantic Skill Score : {candidate['semantic_skill_score']:.4f}")

        print(f"Experience Score     : {candidate['experience_score']:.4f}")

        print(f"Behaviour Score      : {candidate['behaviour_score']:.4f}")

        print(f"Final Score          : {candidate['final_score']:.4f}")

        print("\nCandidate Strengths")

        for reason in candidate["reasons"]:

            print(f"✔ {reason}")

        print("\nAreas of Improvement")

        if len(candidate["missing"]) == 0:

            print("None")

        else:

            for skill in candidate["missing"]:

                print(f"✖ {skill}")

        print()

        print_candidate_profile(candidate["candidate"])

        print("\n")


if __name__ == "__main__":

    main()
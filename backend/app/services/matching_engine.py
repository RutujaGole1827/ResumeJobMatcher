from app.data.job_roles import JOB_ROLES


def calculate_match_score(user_skills, user_exp, job_skills, min_exp):

    user_skills = [s.lower() for s in user_skills]

    total_weight = sum(job_skills.values())

    matched_weight = 0
    missing_skills = []

    # Skill scoring with importance weights
    for skill, weight in job_skills.items():
        if skill in user_skills:
            matched_weight += weight
        else:
            missing_skills.append(skill)

    skill_score = (matched_weight / total_weight) * 100

    # Experience score
    exp_score = 100 if user_exp >= min_exp else (user_exp / min_exp) * 100

    # Final weighted score
    final_score = (skill_score * 0.75) + (exp_score * 0.25)

    return round(final_score, 2), missing_skills


def match_jobs(user_skills, user_exp):

    results = {}

    for job, data in JOB_ROLES.items():
        score, missing = calculate_match_score(
            user_skills, user_exp, data["skills"], data["min_experience"]
        )

        # results[job] = {"score": score, "missing_skills": missing}
        results[job] = {
            "score": score,
            "missing_skills": missing,
            "explanation": explain_match(user_skills, data["skills"].keys()),
        }

    # Sort by score
    sorted_results = dict(
        sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    )

    return sorted_results


# Explaination logic for WHY a score is given.
def explain_match(user_skills, job_skills):

    matched = []
    missing = []

    for skill in job_skills:
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_ratio": f"{len(matched)}/{len(job_skills)}",
    }

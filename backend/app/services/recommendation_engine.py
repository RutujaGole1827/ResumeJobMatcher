def generate_recommendations(job_matches):

    recommendations = {}

    for job, data in job_matches.items():
        missing = data.get("missing_skills", [])

        tips = []

        for skill in missing:
            tips.append(f"Learn {skill} to improve {job} match")

        recommendations[job] = tips

    return recommendations

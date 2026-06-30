import re
from datetime import datetime

# Basic skill database (we will improve later with ML)
SKILLS_DB = [
    "python",
    "java",
    "fastapi",
    "flask",
    "django",
    "sql",
    "mysql",
    "postgresql",
    "machine learning",
    "deep learning",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "angular",
    "react",
    "node",
    "express",
]


def extract_skills(text: str):
    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))


# extract the experienceYears from the duration given for each experience in resume
def extract_experience_from_dates(text: str):
    text = text.lower()

    # matches patterns like:
    # 2020 - 2023
    # 2021- current
    # 2019 – 2022

    pattern = r"(20\d{2})\s*[-–]\s*(20\d{2}|present|current)"

    matches = re.findall(pattern, text)

    total_years = 0
    current_year = datetime.now().year

    for start, end in matches:
        start_year = int(start)

        if end in ["present", "current"]:
            end_year = current_year
        else:
            end_year = int(end)

        total_years += max(0, end_year - start_year)

    return total_years


# extract Total experience


def extract_experience(text: str):
    text = text.lower()

    # Method 1: explicit "X years experience"
    patterns = [
        r"(\d+)\+?\s+years?\s+of\s+experience",
        r"(\d+)\+?\s+years?\s+experience",
        r"experience\s*:\s*(\d+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    # Method 2: timeline-based extraction (NEW)
    return extract_experience_from_dates(text)

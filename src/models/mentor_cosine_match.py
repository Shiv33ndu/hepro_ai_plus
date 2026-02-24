import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


STUDENT_NEED_VECTORS = {
    0: np.array([0.9, 0.5, 0.6, 0.8]),  # Academic performers
    1: np.array([0.5, 0.6, 0.9, 0.9]),  # Directionless
    2: np.array([0.6, 1.0, 0.4, 0.5])   # Burnout
}


MENTOR_CAPABILITY_VECTORS = {
    "academic":     np.array([1.0, 0.4, 0.6, 0.7]),
    "career":       np.array([0.6, 0.5, 0.6, 1.0]),
    "productivity": np.array([0.5, 0.5, 1.0, 0.6]),
    "wellness":     np.array([0.4, 1.0, 0.4, 0.5])
}


def select_mentor_cosine(mentors, cluster):
    """Hybrid selection using rules + cosine similarity."""

    need_vector = STUDENT_NEED_VECTORS[cluster]

    # --- Tier 1: Capacity filter ---
    candidates = mentors[
        mentors["current_load"] < mentors["max_capacity"]
    ].copy()

    if candidates.empty:
        return None

    # --- Compute similarity for each candidate ---
    similarities = []

    for _, mentor in candidates.iterrows():
        capability = MENTOR_CAPABILITY_VECTORS[mentor["expertise"]]

        sim = cosine_similarity(
            need_vector.reshape(1, -1),
            capability.reshape(1, -1)
        )[0][0]

        similarities.append(sim)

    candidates["similarity"] = similarities

    # --- Select best mentor ---
    mentor = candidates.sort_values(
        by=["similarity", "availability_hours"],
        ascending=[False, False]
    ).iloc[0]

    return mentor



def match_students_cosine(students:pd.DataFrame, mentors:pd.DataFrame):

    mentors = mentors.copy()
    results = []

    for _, student in students.iterrows():

        cluster = student["cluster"]
        risk = student["risk_category"]

        mentor = select_mentor_cosine(mentors, cluster)

        if mentor is not None:
            mentor_id = mentor["mentor_id"]
            mentor_name = mentor["name"]

            mentors.loc[
                mentors["mentor_id"] == mentor_id,
                "current_load"
            ] += 1

            status = "Assigned"
        else:
            mentor_id = None
            mentor_name = "Pending Assignment"
            status = "Pending"

        results.append({
            "student_id": student["student_id"],
            "cluster": cluster,
            "risk_category": risk,
            "mentor_id": mentor_id,
            "mentor_name": mentor_name,
            "assignment_status": status
        })

    return pd.DataFrame(results)
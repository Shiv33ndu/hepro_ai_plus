import numpy as np
import pandas as pd
import random

from src.utils.helpers import sample_range

# import student's archetypes and programs
from src.utils.constants import ARCHETYPES, PROGRAMS



def generate_student(student_id: int, archetype_name: str):
    
    archetype = ARCHETYPES[archetype_name]
    programs = random.choice(list(PROGRAMS.keys()))
    max_sem = PROGRAMS[programs]["total_semesters"]

    # student schema
    student = {
    "student_id": f"S{str(student_id).zfill(3)}",
    "age": random.randint(18, 24),
    "program": programs,
    "semester": random.randint(1, max_sem),

    "gpa": sample_range(*archetype["gpa"]),
    "attendance": sample_range(*archetype["attendance"]),
    "assignment_completion": sample_range(*archetype["assignment_completion"]),
    "engagement_score": sample_range(*archetype["engagement_score"]),
    "stress_level": random.randint(*archetype["stress_level"]),
    "career_clarity": random.randint(*archetype["career_clarity"])
}
    
    # sleep hours relate to stress level
    student["sleep_hours"] = round(
        max(4, 8 - (student["stress_level"] * 0.4)), 
        1
    )

    # mental wellbeing depends on strees level
    student["mental_wellbeing"] = max(
        1,
        10 - student["stress_level"] + random.randint(-1, 1)
    )

    # productivity depends on assignment
    student["productivity_score"] = max(
        1,
        int(
            (student["assignment_completion"] / 20) - random.randint(0, 2)
        )
    )

    # distraction inversely depends on productivity
    student["distractions"] = max(
        1,
        10 - student["productivity_score"] + random.randint(-1, 1)
    )


    return student
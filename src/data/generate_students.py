import numpy as np
import pandas as pd
import random

from src.utils.helpers import sample_range

# import student's archetypes and programs
from src.utils.constants import ARCHETYPES, PROGRAMS



def generate_student(student_id: int, archetype_name: str):
    """
    generates single student data
    
    :param student_id: student id, unique identifier
    :type student_id: int
    :param archetype_name: student archetype
    :type archetype_name: str

    returns
    student : dictionary of student data
    """
    
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



def generate_dataset(students_per_archetype: int=15):
    """
    generates realistic synthetic dataset
    
    :param students_per_archetype: No of students per archetypes
    :type students_per_archetype: int

    returns 
    student dataframe containing (archetypes * students_per_archetypes) rows 
    """

    students = []
    student_id = 1

    for archetype in ARCHETYPES.keys():
        for _ in range(students_per_archetype):
            students.append(generate_student(student_id, archetype))
            student_id += 1

    return pd.DataFrame(students)
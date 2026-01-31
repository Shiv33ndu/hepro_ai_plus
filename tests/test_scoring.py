import pandas as pd
from src.scoring.academic_score import academic_score
from src.scoring.wellness_score import wellness_score
from src.scoring.productivity_score import productivity_time_management_score

"""
Classification threshold 

Green  ≥ 80
Blue   65-79
Yellow 45-64
Red    < 45

"""

# APS scoring unit test
def test_aps_high_performer():
    df = pd.DataFrame({
        'gpa': [9.0],
        'attendance': [90],
        'assignment_completion': [95]
    })

    aps = academic_score(df).iloc[0]

    assert aps > 85


# WWS scoring unit test 
def test_wws_burned_out_student():
    df = pd.DataFrame({
        'stress_level': [9],
        'sleep_hours': [4],
        'mental_wellbeing': [3]
    })

    wws = wellness_score(df).iloc[0]

    assert wws < 64



# PTMS scoring unit test
def test_ptms_high_productivity():
    df = pd.DataFrame({
        "productivity_score":[8],
        "distractions": [3]
    })

    ptms = productivity_time_management_score(df).iloc[0]

    print(ptms)

    assert ptms > 70
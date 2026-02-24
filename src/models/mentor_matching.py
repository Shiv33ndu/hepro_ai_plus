import pandas as pd 


def determine_students_need(cluster: int) -> str:
    """
    Map the cluster to required mentorship type 
    
    :param cluster: Students cluster  
    :type cluster: int

    Returns:
        The required mentorship type (wellness/career/academic)
    """

    if cluster == 2:
        return "wellness"   # for burnout students wellness mentorship is the priority
    elif cluster == 1:
        return "career"     # disengaged students need career and productivity direction
    elif cluster == 0:
        return "career"     # academic performers need only career direction 
    else:
        return "academic"


def determine_intervention_type(cluster: int) -> str:
    """
    The type of intervetion needed from the mentors as per the student cluster.
        
    :param cluster: students cluster group 
    :type cluster: int
    :return: The type of intervention students need
    :rtype: str
    """
    
    if cluster == 2:                    # for burnout students group
        return "Wellness Stabilization"
    elif cluster == 1:                  # for disengaged students group
        return "Career Direction & Productivity Coaching"
    elif cluster == 0:                  # for academically good students
        return "Career Direction"
    else:
        return "Acedamic Optimization & Career Planning"



def determine_urgency(risk:str, cluster: int) -> bool:
    """
    Determines whether the student's case is urgent or not 
    
    :return: True or False for urgent case
    :rtype: boolean
    """

    if risk == "Red" or cluster == 2:
        return True
    return False



def select_mentor(mentors:pd.DataFrame, risk:str, expertise:str) -> pd.Series:
    """
    Select the best available mentor matching constraints.
    
    :return: Returns the series of best available mentor 
    :rtype: Series[Any]
    """

    # we first look for all the matching mentors as per risk and expertise
    candidates = mentors[
        (mentors["expertise"] == expertise) &
        (mentors["priority_levels"].str.contains(risk)) &
        (mentors["current_load"] < mentors["max_capacity"])
        ]
    
    if candidates.empty:
        # --- Tier 2: Ignore risk filter ---
        candidates = mentors[
            (mentors["expertise"] == expertise) &
            (mentors["current_load"] < mentors["max_capacity"])
        ]

    if candidates.empty:
        # --- Tier 3: Any available mentor ---
        candidates = mentors[
            mentors["current_load"] < mentors["max_capacity"]
        ]
    # if no match found for the student, return None
    if candidates.empty:
        return None

    # we look for best available mentor out of matching mentor list
    mentor = candidates.sort_values("availability_hours", ascending=False).iloc[0]

    return mentor



def match_mentor(students:pd.DataFrame, mentors:pd.DataFrame) -> pd.DataFrame:
    """
    Match mentor for each student
    
    :param students: student dataset
    :type students: pd.DataFrame
    :param mentors: mentors dataset
    :type mentors: pd.DataFrame
    :return: recommendation datatset
    :rtype: DataFrame
    """

    if students.empty:
        raise ValueError("Student dataset is empty!")
    
    if mentors.empty:
        raise ValueError("Mentors dataset is empty!")
    

    recommendations = []

    for _, student in students.iterrows():

        cluster = student["cluster"]
        risk = student["risk_category"]

        mentorship_need = determine_students_need(cluster)
        intervention_type = determine_intervention_type(cluster)
        is_urgent = determine_urgency(risk, cluster)

        mentor = select_mentor(mentors, risk, mentorship_need)

        if mentor is not None:
            mentor_id = mentor["mentor_id"]
            mentor_name = mentor["name"]

            # we need to update the count of students assigned
            mentors.loc[
                mentors["mentor_id"] == mentor_id,
                "current_load"
            ] += 1
        
        else:
            mentor_id = None
            mentor_name = "Pending Assignment"

        recommendations.append({
            "student_id": student["student_id"],
            "cluster": cluster,
            "risk_category": risk,
            "mentor_id": mentor_id if mentor_id else None,
            "mentor_name": mentor_name,
            "mentor_expertise": mentorship_need,
            "intervention": intervention_type,
            "assignment_status": "Assigend" if mentor_id else "Pending",
            "alert": is_urgent
        })

    return pd.DataFrame(recommendations)
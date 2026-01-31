import pandas as pd

def academic_score(df: pd.DataFrame) -> pd.Series:
    """
    Compute Academic Performance Score (APS).

    APS Combines:
    - GPA (normalized 0-100)
    - Assignment completion (%)
    - Attendance (%) 
    
    Returns:
        pd.Series: APS values on a 0-100 scale
    """

    if df.empty:
        raise ValueError("Dataframe is empty!!")
    
    required_cols = {"gpa", "assignment_completion", "attendance"}

    missing = required_cols - set(df.columns)

    if missing:
        raise KeyError(f"Missing required columns {missing}")
    
    gpa_norm = (df['gpa'] / 10) * 100

    aps = (
        0.5 * gpa_norm
        + 0.3 * df['assignment_completion']
        + 0.2 * df['attendance']
    )

    return aps.round(2)
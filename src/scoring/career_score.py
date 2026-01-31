import pandas as pd

def career_score(df:pd.DataFrame) -> pd.Series:
    """
    Computes Career Readiness Score (CRS).

    CRS combines:
    - Career clarity (1-10)
    - Skill readiness (1-10) 
    
    Returns:
        pd.Series: CRS values on a 0-100 scale
    """

    if df.empty:
        raise ValueError("Input Dataframe is empty.")
    
    required_cols = {"career_clarity", "skill_readiness"}
    missing = required_cols - set(df.columns)

    if missing:
        raise KeyError(f"Missing columns {missing}")
    
    career_norm = (df['career_clarity'] / 10) * 100
    skill_norm = (df['skill_readiness'] / 10) * 100

    crs = (0.5 * career_norm) + (0.5 * skill_norm)

    return crs.round(2)
import pandas as pd

def wellness_score(df: pd.DataFrame) -> pd.Series:
    """
    Compute wellness & wellbeing score (WWS).

    WWS combines:
    - Stress level (inverted, 1-10, strees_norm : high stress -> low score)
    - Sleep hours (0-10)
    - Mental Wellbeing (1-10)
    
    Returns:
        pd.Series: WWS values on a 0-100 scale
    """

    if df.empty:
        raise ValueError("Input Dataframe is empty!")
    
    required_cols = {"stress_level", "sleep_hours", "mental_wellbeing"}
    missing = required_cols - set(df.columns)

    if missing:
        raise KeyError(f"Missing columns {missing}")
    
    # we give low score to high stress, and high score to low stress
    stress_norm = (10 - df['stress_level']) * 10

    # normalizing sleep hours in 0 - 100
    sleep_norm = (df['sleep_hours'] / 10) * 100

    # normalizing mental wellbeing in 0-100
    wellbeing_norm = (df["mental_wellbeing"] / 10) * 100

    wws = (
        0.4 * stress_norm
        + 0.3 * sleep_norm
        + 0.3 * wellbeing_norm
    ) 

    return wws.round(2)
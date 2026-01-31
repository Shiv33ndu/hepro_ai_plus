import pandas as pd

def compute_sri(df: pd.DataFrame) -> pd.Series:
    """
    Compute Student Readiness Index (SRI).

    SRI is a weighted combination of:
    - APS (academic score)
    - WWS (wellness score)
    - PTMS (Productivity & Time Management Score)
    - CRS (Career Readiness Score)
    
    Returns:
        pd.Series: SRI values on a 0-100 scale
    """

    if df.empty:
        raise ValueError("Input Dataframe is empty!")
    
    required_col = {"APS", "WWS", "PTMS", "CRS"}
    missing = required_col - set(df.columns)

    if missing:
        raise KeyError(f"Missing columns {missing}")
    
    sri = (
        0.30 * df["APS"]
        + 0.25 * df["WWS"]
        + 0.20 * df["PTMS"]
        + 0.25 * df["CRS"]
    )
    
    return sri.round(2)



def classify_risk(sri: pd.Series) -> pd.Series:
    """
    Classify student into risk categories bases on SRI.

    Threshols:
    - Green  : SRI >= 80
    - BLUE   : 65 <= SRI < 80
    - Yellow : 45 <= SRI < 65
    - Red    : SRI < 45
    
    """
    def _label(score):
        if score >= 80:
            return "Green"
        elif score >= 65:
            return "Blue"
        elif score >= 45:
            return "Yellow"
        else:
            return "Red"
        
    return sri.apply(_label)
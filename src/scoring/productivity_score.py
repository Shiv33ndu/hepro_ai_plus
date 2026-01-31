import pandas as pd

def productivity_time_management_score(df:pd.DataFrame) -> pd.Series:
    """
    Compute productivity & Time Management score (PTMS).
    
    PTMS combines:
    - Productivity score (1-10, positive signal)
    - Distractions (1-10, negative signal, so we will invert it)

    Returns:
        pd.Series: PTMS values on 0-100 scale 
    """

    if df.empty:
        raise ValueError("Input dataframe is empty.")
    
    required_cols = {'productivity_score', 'distractions'}
    missing = required_cols - set(df.columns)

    if missing:
        raise KeyError(f"Missing columns: {missing}")
    
    # its a positive signal
    productivity_norm = (df['productivity_score'] / 10) * 100

    # distractions are negative signals, so we invert it first
    distractions_norm = (10 - df['distractions']) * 10

    ptms = (
        0.6 * productivity_norm
        + 0.4 * distractions_norm
    )

    return ptms.round(2)
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

REQUIRED_FEATURES = ["APS", "WWS", "PTMS", "CRS"]

def perform_cluster(df:pd.DataFrame, n_clusters:int = 4, random_state:int = 42):
    """
    Perform K-Means clustering on engineered features APS, WWS, PTMS, CRS scores.

    Params:
        df (pd.Dataframe): scored students dataset
        n_cluster (int): Number of Clusters
        random_state (int): Seed for reproducibility

    Returns:
        scaler (StandardScaler)
        df_with_clusters (pd.DataFrame)
        kmeans_model (K-Means) 
    """

    if df.empty:
        raise ValueError(f"Dataframe is empty!")
    
    missing = set(REQUIRED_FEATURES) - set(df.columns)

    if missing: 
        raise KeyError(f"Missing required column: {missing}")
    
    X = df[REQUIRED_FEATURES]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(
        n_clusters=n_clusters,
        n_init=10,
        random_state=random_state
    )

    clusters = kmeans.fit_predict(X_scaled)

    df = df.copy()
    df['cluster'] = clusters

    return scaler, df, kmeans
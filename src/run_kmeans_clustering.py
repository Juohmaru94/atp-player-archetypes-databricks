import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_features.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters.csv"

FEATURE_COLS = [
    "win_rate",
    "avg_player_rank",
    "ace_per_match",
    "df_per_match",
    "first_serve_in_rate",
    "first_serve_win_rate",
    "second_serve_win_rate",
    "break_points_saved_rate",
]


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    model_df = df.copy()

    X = model_df[FEATURE_COLS].copy()
    X = X.dropna()

    model_df = model_df.loc[X.index].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    model_df["cluster"] = kmeans.fit_predict(X_scaled)

    model_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved clustered file to: {OUTPUT_FILE}")
    print(f"Shape: {model_df.shape}")
    print("\nCluster counts:")
    print(model_df["cluster"].value_counts().sort_index())
    print("\nPreview:")
    print(model_df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
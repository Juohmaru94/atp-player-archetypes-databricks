import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_season.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_features.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    feature_df = df.copy()

    # simple filter to reduce noisy player-seasons
    feature_df = feature_df[feature_df["matches_played"] >= 10].copy()

    # keep the first clustering feature set small and interpretable
    selected_columns = [
        "season",
        "player_id",
        "player_name",
        "matches_played",
        "wins",
        "losses",
        "win_rate",
        "avg_player_age",
        "avg_player_rank",
        "ace_per_match",
        "df_per_match",
        "first_serve_in_rate",
        "first_serve_win_rate",
        "second_serve_win_rate",
        "break_points_saved_rate",
    ]

    feature_df = feature_df[selected_columns].copy()

    feature_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved archetype feature file to: {OUTPUT_FILE}")
    print(f"Shape: {feature_df.shape}")
    print("\nSeason distribution:")
    print(feature_df["season"].value_counts().sort_index())
    print("\nPlayers kept after minimum match filter:")
    print(feature_df["player_id"].nunique())
    print("\nPreview:")
    print(feature_df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
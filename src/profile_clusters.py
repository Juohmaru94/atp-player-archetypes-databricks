import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "cluster_profiles.csv"

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

    profile_df = (
        df.groupby("cluster", as_index=False)[FEATURE_COLS]
        .mean()
        .sort_values("cluster")
    )

    counts_df = (
        df.groupby("cluster", as_index=False)
        .agg(
            player_seasons=("player_id", "count"),
            unique_players=("player_id", "nunique"),
        )
        .sort_values("cluster")
    )

    final_df = profile_df.merge(counts_df, on="cluster", how="left")
    final_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved cluster profiles to: {OUTPUT_FILE}")
    print("\nCluster profiles:")
    print(final_df.to_string(index=False))


if __name__ == "__main__":
    main()
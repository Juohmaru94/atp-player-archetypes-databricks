import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "first_serve_points_won_by_surface.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()
    df["first_serve_win_rate"] = df["1stWon"] / df["1stIn"]
    df = df[df["first_serve_win_rate"].notna()].copy()

    summary = (
        df.groupby("surface", as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            avg_first_serve_win_rate=("first_serve_win_rate", "mean"),
            avg_win_rate=("won_match", "mean"),
        )
        .sort_values("surface")
    )

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nAverage first serve points won by surface:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
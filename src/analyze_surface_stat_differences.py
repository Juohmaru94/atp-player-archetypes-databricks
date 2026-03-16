import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "surface_stat_differences.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()
    df["first_serve_in_rate"] = df["1stIn"] / df["svpt"]
    df["first_serve_win_rate"] = df["1stWon"] / df["1stIn"]
    second_serve_attempts = df["svpt"] - df["1stIn"]
    df["second_serve_win_rate"] = df["2ndWon"] / second_serve_attempts
    df["break_points_saved_rate"] = df["bpSaved"] / df["bpFaced"]

    summary = (
        df.groupby("surface", as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            avg_first_serve_in_rate=("first_serve_in_rate", "mean"),
            avg_first_serve_win_rate=("first_serve_win_rate", "mean"),
            avg_second_serve_win_rate=("second_serve_win_rate", "mean"),
            avg_break_points_saved_rate=("break_points_saved_rate", "mean"),
            avg_aces=("ace", "mean"),
            avg_double_faults=("df", "mean"),
            avg_minutes=("minutes", "mean"),
        )
        .sort_values("surface")
    )

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nSurface stat differences:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "aces_by_surface.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    summary = (
        df.groupby("surface", as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            avg_aces=("ace", "mean"),
            avg_double_faults=("df", "mean"),
            avg_minutes=("minutes", "mean"),
        )
        .sort_values("surface")
    )

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nAces, double faults, and match length by surface:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "aces_per_match_buckets.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()

    bins = [-0.01, 2, 5, 8, 12, 16, 100]
    labels = [
        "0-1",
        "2-4",
        "5-7",
        "8-11",
        "12-15",
        "16+",
    ]

    df["aces_bucket"] = pd.cut(
        df["ace"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False,
    )

    summary = (
        df.groupby("aces_bucket", observed=False, as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            wins=("won_match", "sum"),
        )
    )

    summary["win_rate"] = summary["wins"] / summary["player_matches"]

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nWin rate by aces bucket:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
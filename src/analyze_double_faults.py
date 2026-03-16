import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "double_fault_buckets.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()

    bins = [-0.01, 2, 4, 6, 8, 10, 100]
    labels = [
        "0-1",
        "2-3",
        "4-5",
        "6-7",
        "8-9",
        "10+",
    ]

    df["double_fault_bucket"] = pd.cut(
        df["df"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False,
    )

    summary = (
        df.groupby("double_fault_bucket", observed=False, as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            wins=("won_match", "sum"),
        )
    )

    summary["win_rate"] = summary["wins"] / summary["player_matches"]

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nWin rate by double fault bucket:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
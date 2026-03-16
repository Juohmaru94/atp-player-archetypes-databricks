import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "break_points_saved_rate_buckets.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()
    df["break_points_saved_rate"] = df["bpSaved"] / df["bpFaced"]
    df = df[df["break_points_saved_rate"].notna()].copy()

    bins = [0.0, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.01]
    labels = [
        "<40%",
        "40-50%",
        "50-60%",
        "60-70%",
        "70-80%",
        "80-90%",
        "90%+",
    ]

    df["break_points_saved_bucket"] = pd.cut(
        df["break_points_saved_rate"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False,
    )

    summary = (
        df.groupby("break_points_saved_bucket", observed=False, as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            wins=("won_match", "sum"),
        )
    )

    summary["win_rate"] = summary["wins"] / summary["player_matches"]

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nWin rate by break points saved rate bucket:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
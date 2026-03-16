import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "first_serve_in_win_rate_buckets.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()
    df["first_serve_in_rate"] = df["1stIn"] / df["svpt"]
    df = df[df["first_serve_in_rate"].notna()].copy()

    bins = [0.0, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 1.01]
    labels = [
        "<50%",
        "50-55%",
        "55-60%",
        "60-65%",
        "65-70%",
        "70-75%",
        "75-80%",
        "80%+",
    ]

    df["first_serve_in_bucket"] = pd.cut(
        df["first_serve_in_rate"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False,
    )

    summary = (
        df.groupby("first_serve_in_bucket", observed=False, as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            wins=("won_match", "sum"),
        )
    )

    summary["win_rate"] = summary["wins"] / summary["player_matches"]

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nWin rate by first serve in bucket:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
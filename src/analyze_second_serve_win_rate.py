import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "second_serve_win_rate_buckets.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df = df.copy()
    second_serve_attempts = df["svpt"] - df["1stIn"]
    df["second_serve_win_rate"] = df["2ndWon"] / second_serve_attempts
    df = df[df["second_serve_win_rate"].notna()].copy()

    bins = [0.0, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 1.01]
    labels = [
        "<40%",
        "40-45%",
        "45-50%",
        "50-55%",
        "55-60%",
        "60-65%",
        "65-70%",
        "70%+",
    ]

    df["second_serve_win_bucket"] = pd.cut(
        df["second_serve_win_rate"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False,
    )

    summary = (
        df.groupby("second_serve_win_bucket", observed=False, as_index=False)
        .agg(
            player_matches=("match_id", "count"),
            wins=("won_match", "sum"),
        )
    )

    summary["win_rate"] = summary["wins"] / summary["player_matches"]

    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved analysis output to: {OUTPUT_FILE}")
    print("\nWin rate by second serve win rate bucket:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
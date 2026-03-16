import pandas as pd

from src.config import PROCESSED_DATA_DIR

FIRST_SERVE_IN_FILE = PROCESSED_DATA_DIR / "first_serve_in_win_rate_buckets.csv"
FIRST_SERVE_WON_FILE = PROCESSED_DATA_DIR / "first_serve_points_won_win_rate_buckets.csv"
SECOND_SERVE_WON_FILE = PROCESSED_DATA_DIR / "second_serve_win_rate_buckets.csv"

OUTPUT_FILE = PROCESSED_DATA_DIR / "insight_summary_table.csv"


def add_metric_name(df: pd.DataFrame, metric_name: str, bucket_col: str) -> pd.DataFrame:
    out = df.copy()
    out["metric"] = metric_name
    out = out.rename(columns={bucket_col: "bucket"})
    return out[["metric", "bucket", "player_matches", "wins", "win_rate"]]


def main() -> None:
    fs_in = pd.read_csv(FIRST_SERVE_IN_FILE)
    fs_won = pd.read_csv(FIRST_SERVE_WON_FILE)
    ss_won = pd.read_csv(SECOND_SERVE_WON_FILE)

    fs_in = add_metric_name(fs_in, "first_serve_in_rate", "first_serve_in_bucket")
    fs_won = add_metric_name(fs_won, "first_serve_points_won_rate", "first_serve_win_bucket")
    ss_won = add_metric_name(ss_won, "second_serve_points_won_rate", "second_serve_win_bucket")

    summary = pd.concat([fs_in, fs_won, ss_won], ignore_index=True)
    summary.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved insight summary table to: {OUTPUT_FILE}")
    print("\nPreview:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
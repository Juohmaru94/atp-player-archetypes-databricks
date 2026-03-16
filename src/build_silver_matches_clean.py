import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "matches_raw_combined.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "matches_clean.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    # standardize column names
    df.columns = [col.strip() for col in df.columns]

    # parse tournament date
    df["tourney_date"] = pd.to_datetime(df["tourney_date"], format="%Y%m%d", errors="coerce")

    # clean string columns
    string_cols = [
        "tourney_id",
        "tourney_name",
        "surface",
        "tourney_level",
        "winner_name",
        "winner_hand",
        "winner_ioc",
        "loser_name",
        "loser_hand",
        "loser_ioc",
        "score",
        "round",
        "source_file",
    ]

    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip()

    # enforce numeric columns
    numeric_cols = [
        "draw_size",
        "match_num",
        "winner_id",
        "winner_seed",
        "winner_ht",
        "winner_age",
        "loser_id",
        "loser_seed",
        "loser_ht",
        "loser_age",
        "best_of",
        "minutes",
        "w_ace",
        "w_df",
        "w_svpt",
        "w_1stIn",
        "w_1stWon",
        "w_2ndWon",
        "w_SvGms",
        "w_bpSaved",
        "w_bpFaced",
        "l_ace",
        "l_df",
        "l_svpt",
        "l_1stIn",
        "l_1stWon",
        "l_2ndWon",
        "l_SvGms",
        "l_bpSaved",
        "l_bpFaced",
        "winner_rank",
        "winner_rank_points",
        "loser_rank",
        "loser_rank_points",
        "season",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # create match_id
    df["match_id"] = (
        df["tourney_id"].astype("string")
        + "_"
        + df["match_num"].astype("Int64").astype("string")
        + "_"
        + df["winner_id"].astype("Int64").astype("string")
        + "_"
        + df["loser_id"].astype("Int64").astype("string")
    )

    # reorder to place match_id first
    cols = ["match_id"] + [col for col in df.columns if col != "match_id"]
    df = df[cols]

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved cleaned matches file to: {OUTPUT_FILE}")
    print(f"Shape: {df.shape}")
    print("\nNulls in key fields:")
    print(
        df[
            [
                "match_id",
                "tourney_id",
                "tourney_date",
                "winner_id",
                "loser_id",
                "season",
            ]
        ].isnull().sum()
    )


if __name__ == "__main__":
    main()
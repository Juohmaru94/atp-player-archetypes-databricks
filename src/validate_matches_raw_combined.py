import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "matches_raw_combined.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    print("Combined raw matches validation")
    print("-" * 50)
    print(f"Shape: {df.shape}")
    print()

    print("Columns:")
    for col in df.columns:
        print(f"- {col}")
    print()

    print("Null counts for key columns:")
    key_cols = [
        "tourney_id",
        "tourney_name",
        "surface",
        "tourney_date",
        "match_num",
        "winner_id",
        "winner_name",
        "loser_id",
        "loser_name",
        "season",
        "source_file",
    ]
    print(df[key_cols].isnull().sum())
    print()

    print("Rows by season:")
    print(df["season"].value_counts().sort_index())
    print()

    print("Unique surfaces:")
    print(sorted(df["surface"].dropna().unique()))
    print()

    print("Unique tourney levels:")
    print(sorted(df["tourney_level"].dropna().unique()))
    print()


if __name__ == "__main__":
    main()
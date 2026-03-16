from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

MATCH_FILES = [
    "atp_matches_2020.csv",
    "atp_matches_2021.csv",
    "atp_matches_2022.csv",
    "atp_matches_2023.csv",
    "atp_matches_2024.csv",
]


def extract_season_from_filename(filename: str) -> int:
    return int(filename.replace("atp_matches_", "").replace(".csv", ""))


def load_single_match_file(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df["source_file"] = file_path.name
    df["season"] = extract_season_from_filename(file_path.name)
    return df


def main() -> None:
    all_dfs = []

    for filename in MATCH_FILES:
        file_path = RAW_DATA_DIR / filename
        df = load_single_match_file(file_path)
        print(f"Loaded {filename}: {df.shape[0]} rows, {df.shape[1]} columns")
        all_dfs.append(df)

    matches_df = pd.concat(all_dfs, ignore_index=True)

    print("\nCombined dataset summary")
    print(f"Rows: {matches_df.shape[0]}")
    print(f"Columns: {matches_df.shape[1]}")
    print("\nRows by season:")
    print(matches_df["season"].value_counts().sort_index())

    output_path = PROCESSED_DATA_DIR / "matches_raw_combined.csv"
    matches_df.to_csv(output_path, index=False)

    print(f"\nSaved combined file to: {output_path}")


if __name__ == "__main__":
    main()
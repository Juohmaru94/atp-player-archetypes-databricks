from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_DIR

MATCH_FILES = [
    "atp_matches_2020.csv",
    "atp_matches_2021.csv",
    "atp_matches_2022.csv",
    "atp_matches_2023.csv",
    "atp_matches_2024.csv",
]

PLAYER_FILE = "atp_players.csv"


def inspect_csv(file_path: Path, nrows: int = 5) -> None:
    print("=" * 100)
    print(f"FILE: {file_path.name}")

    df = pd.read_csv(file_path, nrows=nrows)

    print(f"\nShape (sample): {df.shape}")
    print(f"\nColumns ({len(df.columns)}):")
    for col in df.columns:
        print(f"- {col}")

    print("\nPreview:")
    print(df.head(nrows).to_string(index=False))
    print()


def main() -> None:
    print(f"Inspecting raw files in: {RAW_DATA_DIR}\n")

    for filename in MATCH_FILES:
        inspect_csv(RAW_DATA_DIR / filename, nrows=3)

    inspect_csv(RAW_DATA_DIR / PLAYER_FILE, nrows=3)


if __name__ == "__main__":
    main()

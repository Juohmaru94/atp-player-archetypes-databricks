from pathlib import Path

from src.config import RAW_DATA_DIR

EXPECTED_FILES = [
    "atp_matches_2020.csv",
    "atp_matches_2021.csv",
    "atp_matches_2022.csv",
    "atp_matches_2023.csv",
    "atp_matches_2024.csv",
    "atp_players.csv",
]


def main() -> None:
    print(f"Checking raw data folder: {RAW_DATA_DIR}\n")

    missing = []
    for filename in EXPECTED_FILES:
        file_path = RAW_DATA_DIR / filename
        if file_path.exists():
            print(f"[OK] {filename}")
        else:
            print(f"[MISSING] {filename}")
            missing.append(filename)

    print("\nSummary")
    print(f"Expected files: {len(EXPECTED_FILES)}")
    print(f"Missing files: {len(missing)}")

    if missing:
        print("\nMissing list:")
        for filename in missing:
            print(f"- {filename}")
    else:
        print("\nAll expected raw files are present.")


if __name__ == "__main__":
    main()

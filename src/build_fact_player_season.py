import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "fact_player_season.csv"


def safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    return numerator.div(denominator.where(denominator != 0))


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    grouped = (
        df.groupby(["season", "player_id", "player_name"], as_index=False)
        .agg(
            matches_played=("match_id", "count"),
            wins=("won_match", "sum"),
            avg_player_age=("player_age", "mean"),
            avg_player_rank=("player_rank", "mean"),
            avg_player_rank_points=("player_rank_points", "mean"),
            total_ace=("ace", "sum"),
            total_df=("df", "sum"),
            total_svpt=("svpt", "sum"),
            total_1stIn=("1stIn", "sum"),
            total_1stWon=("1stWon", "sum"),
            total_2ndWon=("2ndWon", "sum"),
            total_SvGms=("SvGms", "sum"),
            total_bpSaved=("bpSaved", "sum"),
            total_bpFaced=("bpFaced", "sum"),
            total_opp_ace=("opp_ace", "sum"),
            total_opp_df=("opp_df", "sum"),
            total_opp_svpt=("opp_svpt", "sum"),
            total_opp_1stIn=("opp_1stIn", "sum"),
            total_opp_1stWon=("opp_1stWon", "sum"),
            total_opp_2ndWon=("opp_2ndWon", "sum"),
            total_opp_SvGms=("opp_SvGms", "sum"),
            total_opp_bpSaved=("opp_bpSaved", "sum"),
            total_opp_bpFaced=("opp_bpFaced", "sum"),
        )
    )

    grouped["losses"] = grouped["matches_played"] - grouped["wins"]
    grouped["win_rate"] = safe_divide(grouped["wins"], grouped["matches_played"])

    grouped["ace_per_match"] = safe_divide(grouped["total_ace"], grouped["matches_played"])
    grouped["df_per_match"] = safe_divide(grouped["total_df"], grouped["matches_played"])

    grouped["first_serve_in_rate"] = safe_divide(grouped["total_1stIn"], grouped["total_svpt"])
    grouped["first_serve_win_rate"] = safe_divide(grouped["total_1stWon"], grouped["total_1stIn"])

    second_serve_attempts = grouped["total_svpt"] - grouped["total_1stIn"]
    grouped["second_serve_win_rate"] = safe_divide(grouped["total_2ndWon"], second_serve_attempts)

    grouped["break_points_saved_rate"] = safe_divide(grouped["total_bpSaved"], grouped["total_bpFaced"])

    grouped.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved fact player season file to: {OUTPUT_FILE}")
    print(f"Shape: {grouped.shape}")
    print("\nSeason distribution:")
    print(grouped["season"].value_counts().sort_index())
    print("\nPreview:")
    print(grouped.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
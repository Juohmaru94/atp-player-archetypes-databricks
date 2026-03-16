import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "matches_clean.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"


MATCH_CONTEXT_COLS = [
    "match_id",
    "tourney_id",
    "tourney_name",
    "surface",
    "draw_size",
    "tourney_level",
    "tourney_date",
    "match_num",
    "score",
    "best_of",
    "round",
    "minutes",
    "source_file",
    "season",
]


def build_winner_side(df: pd.DataFrame) -> pd.DataFrame:
    winner_df = df[MATCH_CONTEXT_COLS].copy()

    winner_df["player_id"] = df["winner_id"]
    winner_df["player_name"] = df["winner_name"]
    winner_df["player_hand"] = df["winner_hand"]
    winner_df["player_ht"] = df["winner_ht"]
    winner_df["player_age"] = df["winner_age"]
    winner_df["player_rank"] = df["winner_rank"]
    winner_df["player_rank_points"] = df["winner_rank_points"]

    winner_df["opponent_id"] = df["loser_id"]
    winner_df["opponent_name"] = df["loser_name"]
    winner_df["opponent_hand"] = df["loser_hand"]
    winner_df["opponent_ht"] = df["loser_ht"]
    winner_df["opponent_age"] = df["loser_age"]
    winner_df["opponent_rank"] = df["loser_rank"]
    winner_df["opponent_rank_points"] = df["loser_rank_points"]

    winner_df["won_match"] = 1

    winner_df["ace"] = df["w_ace"]
    winner_df["df"] = df["w_df"]
    winner_df["svpt"] = df["w_svpt"]
    winner_df["1stIn"] = df["w_1stIn"]
    winner_df["1stWon"] = df["w_1stWon"]
    winner_df["2ndWon"] = df["w_2ndWon"]
    winner_df["SvGms"] = df["w_SvGms"]
    winner_df["bpSaved"] = df["w_bpSaved"]
    winner_df["bpFaced"] = df["w_bpFaced"]

    winner_df["opp_ace"] = df["l_ace"]
    winner_df["opp_df"] = df["l_df"]
    winner_df["opp_svpt"] = df["l_svpt"]
    winner_df["opp_1stIn"] = df["l_1stIn"]
    winner_df["opp_1stWon"] = df["l_1stWon"]
    winner_df["opp_2ndWon"] = df["l_2ndWon"]
    winner_df["opp_SvGms"] = df["l_SvGms"]
    winner_df["opp_bpSaved"] = df["l_bpSaved"]
    winner_df["opp_bpFaced"] = df["l_bpFaced"]

    return winner_df


def build_loser_side(df: pd.DataFrame) -> pd.DataFrame:
    loser_df = df[MATCH_CONTEXT_COLS].copy()

    loser_df["player_id"] = df["loser_id"]
    loser_df["player_name"] = df["loser_name"]
    loser_df["player_hand"] = df["loser_hand"]
    loser_df["player_ht"] = df["loser_ht"]
    loser_df["player_age"] = df["loser_age"]
    loser_df["player_rank"] = df["loser_rank"]
    loser_df["player_rank_points"] = df["loser_rank_points"]

    loser_df["opponent_id"] = df["winner_id"]
    loser_df["opponent_name"] = df["winner_name"]
    loser_df["opponent_hand"] = df["winner_hand"]
    loser_df["opponent_ht"] = df["winner_ht"]
    loser_df["opponent_age"] = df["winner_age"]
    loser_df["opponent_rank"] = df["winner_rank"]
    loser_df["opponent_rank_points"] = df["winner_rank_points"]

    loser_df["won_match"] = 0

    loser_df["ace"] = df["l_ace"]
    loser_df["df"] = df["l_df"]
    loser_df["svpt"] = df["l_svpt"]
    loser_df["1stIn"] = df["l_1stIn"]
    loser_df["1stWon"] = df["l_1stWon"]
    loser_df["2ndWon"] = df["l_2ndWon"]
    loser_df["SvGms"] = df["l_SvGms"]
    loser_df["bpSaved"] = df["l_bpSaved"]
    loser_df["bpFaced"] = df["l_bpFaced"]

    loser_df["opp_ace"] = df["w_ace"]
    loser_df["opp_df"] = df["w_df"]
    loser_df["opp_svpt"] = df["w_svpt"]
    loser_df["opp_1stIn"] = df["w_1stIn"]
    loser_df["opp_1stWon"] = df["w_1stWon"]
    loser_df["opp_2ndWon"] = df["w_2ndWon"]
    loser_df["opp_SvGms"] = df["w_SvGms"]
    loser_df["opp_bpSaved"] = df["w_bpSaved"]
    loser_df["opp_bpFaced"] = df["w_bpFaced"]

    return loser_df


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    winner_df = build_winner_side(df)
    loser_df = build_loser_side(df)

    fact_df = pd.concat([winner_df, loser_df], ignore_index=True)

    fact_df = fact_df.sort_values(["season", "tourney_date", "match_id", "won_match"], ascending=[True, True, True, False])

    fact_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved fact player match file to: {OUTPUT_FILE}")
    print(f"Shape: {fact_df.shape}")
    print("\nwon_match value counts:")
    print(fact_df["won_match"].value_counts().sort_index())
    print("\nUnique players:", fact_df["player_id"].nunique())
    print("Unique matches:", fact_df["match_id"].nunique())


if __name__ == "__main__":
    main()
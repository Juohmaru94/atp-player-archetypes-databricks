import sys

import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_MATCH_FILE = PROCESSED_DATA_DIR / "fact_player_match.csv"
INPUT_CLUSTER_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters_labeled.csv"
OUTPUT_DIR = PROCESSED_DATA_DIR


def safe_divide(numerator: float, denominator: float) -> float:
    if pd.isna(denominator) or denominator == 0:
        return None
    return numerator / denominator


def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError("Please provide a player name, e.g. python -m src.build_player_case_study 'Novak Djokovic'")

    player_name = sys.argv[1]

    match_df = pd.read_csv(INPUT_MATCH_FILE)
    cluster_df = pd.read_csv(INPUT_CLUSTER_FILE)

    player_df = match_df[match_df["player_name"] == player_name].copy()

    if player_df.empty:
        raise ValueError(f"No rows found for player: {player_name}")

    summary = {
        "player_name": player_name,
        "matches_played": int(player_df["match_id"].count()),
        "wins": int(player_df["won_match"].sum()),
        "losses": int(player_df["match_id"].count() - player_df["won_match"].sum()),
        "win_rate": player_df["won_match"].mean(),
        "avg_rank": player_df["player_rank"].mean(),
        "avg_aces": player_df["ace"].mean(),
        "avg_double_faults": player_df["df"].mean(),
        "avg_minutes": player_df["minutes"].mean(),
        "first_serve_in_rate": safe_divide(player_df["1stIn"].sum(), player_df["svpt"].sum()),
        "first_serve_win_rate": safe_divide(player_df["1stWon"].sum(), player_df["1stIn"].sum()),
        "second_serve_win_rate": safe_divide(
            player_df["2ndWon"].sum(),
            (player_df["svpt"].sum() - player_df["1stIn"].sum()),
        ),
        "break_points_saved_rate": safe_divide(player_df["bpSaved"].sum(), player_df["bpFaced"].sum()),
    }

    summary_df = pd.DataFrame([summary])

    surface_df = (
        player_df.groupby("surface", as_index=False)
        .agg(
            matches_played=("match_id", "count"),
            wins=("won_match", "sum"),
            avg_aces=("ace", "mean"),
            avg_double_faults=("df", "mean"),
            avg_minutes=("minutes", "mean"),
        )
        .sort_values("surface")
    )
    surface_df["win_rate"] = surface_df["wins"] / surface_df["matches_played"]

    season_df = (
        player_df.groupby("season", as_index=False)
        .agg(
            matches_played=("match_id", "count"),
            wins=("won_match", "sum"),
            avg_rank=("player_rank", "mean"),
            avg_aces=("ace", "mean"),
            avg_double_faults=("df", "mean"),
        )
        .sort_values("season")
    )
    season_df["win_rate"] = season_df["wins"] / season_df["matches_played"]

    cluster_player_df = cluster_df[cluster_df["player_name"] == player_name].copy()

    safe_player_name = player_name.lower().replace(" ", "_")

    summary_file = OUTPUT_DIR / f"{safe_player_name}_case_study_summary.csv"
    surface_file = OUTPUT_DIR / f"{safe_player_name}_case_study_surface.csv"
    season_file = OUTPUT_DIR / f"{safe_player_name}_case_study_season.csv"
    cluster_file = OUTPUT_DIR / f"{safe_player_name}_case_study_clusters.csv"

    summary_df.to_csv(summary_file, index=False)
    surface_df.to_csv(surface_file, index=False)
    season_df.to_csv(season_file, index=False)
    cluster_player_df.to_csv(cluster_file, index=False)

    print(f"Saved summary to: {summary_file}")
    print(summary_df.to_string(index=False))

    print(f"\nSaved surface summary to: {surface_file}")
    print(surface_df.to_string(index=False))

    print(f"\nSaved season summary to: {season_file}")
    print(season_df.to_string(index=False))

    print(f"\nSaved cluster history to: {cluster_file}")
    if cluster_player_df.empty:
        print("No cluster rows found for this player.")
    else:
        print(
            cluster_player_df[
                ["season", "player_name", "cluster", "cluster_label"]
            ].sort_values("season").to_string(index=False)
        )


if __name__ == "__main__":
    main()
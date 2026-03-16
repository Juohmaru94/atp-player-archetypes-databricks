import matplotlib.pyplot as plt
import pandas as pd

from src.config import PROCESSED_DATA_DIR, PROJECT_ROOT

CHARTS_DIR = PROJECT_ROOT / "docs" / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

CLUSTERS_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters_labeled.csv"
PROFILES_FILE = PROCESSED_DATA_DIR / "cluster_profiles.csv"


def save_cluster_counts_chart(df: pd.DataFrame) -> None:
    counts = df["cluster_label"].value_counts().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(counts.index, counts.values)
    plt.title("Player-Season Counts by Archetype")
    plt.xlabel("Archetype")
    plt.ylabel("Player-Seasons")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "cluster_player_season_counts.png")
    plt.close()


def save_cluster_win_rate_chart(df: pd.DataFrame) -> None:
    summary = (
        df.groupby("cluster_label", as_index=False)["win_rate"]
        .mean()
        .sort_values("win_rate", ascending=False)
    )

    plt.figure(figsize=(10, 6))
    plt.bar(summary["cluster_label"], summary["win_rate"])
    plt.title("Average Win Rate by Archetype")
    plt.xlabel("Archetype")
    plt.ylabel("Average Win Rate")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "cluster_average_win_rate.png")
    plt.close()


def save_cluster_ace_profile_chart(df: pd.DataFrame) -> None:
    summary = (
        df.groupby("cluster_label", as_index=False)[["ace_per_match", "df_per_match"]]
        .mean()
        .sort_values("ace_per_match", ascending=False)
    )

    x = range(len(summary))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width / 2 for i in x], summary["ace_per_match"], width=width, label="Aces per Match")
    plt.bar([i + width / 2 for i in x], summary["df_per_match"], width=width, label="Double Faults per Match")

    plt.xticks(list(x), summary["cluster_label"], rotation=25, ha="right")
    plt.title("Serve Risk/Reward Profile by Archetype")
    plt.xlabel("Archetype")
    plt.ylabel("Average Count per Match")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "cluster_serve_risk_reward_profile.png")
    plt.close()


def save_cluster_serve_rates_chart(df: pd.DataFrame) -> None:
    summary = (
        df.groupby("cluster_label", as_index=False)[
            ["first_serve_in_rate", "first_serve_win_rate", "second_serve_win_rate"]
        ]
        .mean()
    )

    plot_df = summary.set_index("cluster_label").T

    plt.figure(figsize=(10, 6))
    for cluster in plot_df.columns:
        plt.plot(plot_df.index, plot_df[cluster], marker="o", label=cluster)

    plt.title("Serve Rate Profile by Archetype")
    plt.xlabel("Metric")
    plt.ylabel("Average Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "cluster_serve_rate_profile.png")
    plt.close()


def main() -> None:
    clusters_df = pd.read_csv(CLUSTERS_FILE)
    profiles_df = pd.read_csv(PROFILES_FILE)

    save_cluster_counts_chart(clusters_df)
    save_cluster_win_rate_chart(clusters_df)
    save_cluster_ace_profile_chart(clusters_df)
    save_cluster_serve_rates_chart(clusters_df)

    print(f"Cluster charts saved to: {CHARTS_DIR}")
    print("\nArchetypes found:")
    for label in sorted(clusters_df["cluster_label"].dropna().unique()):
        print(f"- {label}")


if __name__ == "__main__":
    main()
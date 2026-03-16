import matplotlib.pyplot as plt
import pandas as pd

from src.config import PROCESSED_DATA_DIR, PROJECT_ROOT

CHARTS_DIR = PROJECT_ROOT / "docs" / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)


TSITSIPAS_SUMMARY = PROCESSED_DATA_DIR / "stefanos_tsitsipas_case_study_summary.csv"
MEDVEDEV_SUMMARY = PROCESSED_DATA_DIR / "daniil_medvedev_case_study_summary.csv"

TSITSIPAS_SURFACE = PROCESSED_DATA_DIR / "stefanos_tsitsipas_case_study_surface.csv"
MEDVEDEV_SURFACE = PROCESSED_DATA_DIR / "daniil_medvedev_case_study_surface.csv"


def load_summary_comparison() -> pd.DataFrame:
    ts = pd.read_csv(TSITSIPAS_SUMMARY)
    md = pd.read_csv(MEDVEDEV_SUMMARY)
    combined = pd.concat([ts, md], ignore_index=True)
    return combined


def save_overall_win_rate_chart(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 6))
    plt.bar(df["player_name"], df["win_rate"])
    plt.title("Overall Win Rate: Tsitsipas vs Medvedev")
    plt.xlabel("Player")
    plt.ylabel("Win Rate")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "player_comparison_overall_win_rate.png")
    plt.close()


def save_serve_profile_chart(df: pd.DataFrame) -> None:
    metrics = ["first_serve_in_rate", "first_serve_win_rate", "second_serve_win_rate"]
    plot_df = df[["player_name"] + metrics].set_index("player_name").T

    plt.figure(figsize=(10, 6))
    for player in plot_df.columns:
        plt.plot(plot_df.index, plot_df[player], marker="o", label=player)

    plt.title("Serve Profile Comparison: Tsitsipas vs Medvedev")
    plt.xlabel("Metric")
    plt.ylabel("Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "player_comparison_serve_profile.png")
    plt.close()


def save_surface_win_rate_chart() -> None:
    ts = pd.read_csv(TSITSIPAS_SURFACE)
    md = pd.read_csv(MEDVEDEV_SURFACE)

    merged = ts[["surface", "win_rate"]].merge(
        md[["surface", "win_rate"]],
        on="surface",
        suffixes=("_tsitsipas", "_medvedev"),
    ).sort_values("surface")

    x = range(len(merged))
    width = 0.35

    plt.figure(figsize=(8, 6))
    plt.bar([i - width / 2 for i in x], merged["win_rate_tsitsipas"], width=width, label="Stefanos Tsitsipas")
    plt.bar([i + width / 2 for i in x], merged["win_rate_medvedev"], width=width, label="Daniil Medvedev")

    plt.xticks(list(x), merged["surface"])
    plt.title("Surface Win Rate Comparison")
    plt.xlabel("Surface")
    plt.ylabel("Win Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "player_comparison_surface_win_rate.png")
    plt.close()


def save_surface_aces_chart() -> None:
    ts = pd.read_csv(TSITSIPAS_SURFACE)
    md = pd.read_csv(MEDVEDEV_SURFACE)

    merged = ts[["surface", "avg_aces"]].merge(
        md[["surface", "avg_aces"]],
        on="surface",
        suffixes=("_tsitsipas", "_medvedev"),
    ).sort_values("surface")

    x = range(len(merged))
    width = 0.35

    plt.figure(figsize=(8, 6))
    plt.bar([i - width / 2 for i in x], merged["avg_aces_tsitsipas"], width=width, label="Stefanos Tsitsipas")
    plt.bar([i + width / 2 for i in x], merged["avg_aces_medvedev"], width=width, label="Daniil Medvedev")

    plt.xticks(list(x), merged["surface"])
    plt.title("Surface Ace Comparison")
    plt.xlabel("Surface")
    plt.ylabel("Average Aces")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "player_comparison_surface_aces.png")
    plt.close()


def main() -> None:
    summary_df = load_summary_comparison()
    save_overall_win_rate_chart(summary_df)
    save_serve_profile_chart(summary_df)
    save_surface_win_rate_chart()
    save_surface_aces_chart()
    print(f"Player comparison charts saved to: {CHARTS_DIR}")


if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt

from src.config import PROCESSED_DATA_DIR, PROJECT_ROOT

CHARTS_DIR = PROJECT_ROOT / "docs" / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def save_first_serve_in_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "first_serve_in_win_rate_buckets.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["first_serve_in_bucket"], df["win_rate"])
    plt.title("Win Rate by First Serve In Percentage Bucket")
    plt.xlabel("First Serve In Percentage Bucket")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_rate_by_first_serve_in_bucket.png")
    plt.close()


def save_first_serve_points_won_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "first_serve_points_won_win_rate_buckets.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["first_serve_win_bucket"], df["win_rate"])
    plt.title("Win Rate by First Serve Points Won Percentage Bucket")
    plt.xlabel("First Serve Points Won Percentage Bucket")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_rate_by_first_serve_points_won_bucket.png")
    plt.close()


def save_second_serve_points_won_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "second_serve_win_rate_buckets.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["second_serve_win_bucket"], df["win_rate"])
    plt.title("Win Rate by Second Serve Points Won Percentage Bucket")
    plt.xlabel("Second Serve Points Won Percentage Bucket")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_rate_by_second_serve_points_won_bucket.png")
    plt.close()


def save_aces_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "aces_per_match_buckets.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["aces_bucket"], df["win_rate"])
    plt.title("Win Rate by Ace Bucket")
    plt.xlabel("Ace Bucket")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_rate_by_aces_bucket.png")
    plt.close()


def save_double_fault_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "double_fault_buckets.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["double_fault_bucket"], df["win_rate"])
    plt.title("Win Rate by Double Fault Bucket")
    plt.xlabel("Double Fault Bucket")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_rate_by_double_fault_bucket.png")
    plt.close()


def save_surface_aces_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "aces_by_surface.csv")

    plt.figure(figsize=(8, 6))
    plt.bar(df["surface"], df["avg_aces"])
    plt.title("Average Aces by Surface")
    plt.xlabel("Surface")
    plt.ylabel("Average Aces")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "average_aces_by_surface.png")
    plt.close()


def save_surface_first_serve_chart() -> None:
    df = pd.read_csv(PROCESSED_DATA_DIR / "surface_stat_differences.csv")

    plt.figure(figsize=(8, 6))
    plt.bar(df["surface"], df["avg_first_serve_win_rate"])
    plt.title("Average First Serve Points Won Rate by Surface")
    plt.xlabel("Surface")
    plt.ylabel("Average First Serve Points Won Rate")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "average_first_serve_points_won_rate_by_surface.png")
    plt.close()


def main() -> None:
    save_first_serve_in_chart()
    save_first_serve_points_won_chart()
    save_second_serve_points_won_chart()
    save_aces_chart()
    save_double_fault_chart()
    save_surface_aces_chart()
    save_surface_first_serve_chart()

    print(f"Charts saved to: {CHARTS_DIR}")


if __name__ == "__main__":
    main()
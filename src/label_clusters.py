import pandas as pd

from src.config import PROCESSED_DATA_DIR

INPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "player_archetype_clusters_labeled.csv"

CLUSTER_LABELS = {
    0: "High-Risk Big Server",
    1: "Balanced All-Court Player",
    2: "Lower-Power Grinder",
    3: "Elite Big Server",
}


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    df["cluster_label"] = df["cluster"].map(CLUSTER_LABELS)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved labeled clusters to: {OUTPUT_FILE}")
    print("\nCluster label counts:")
    print(df["cluster_label"].value_counts())
    print("\nPreview:")
    print(
        df[
            [
                "season",
                "player_id",
                "player_name",
                "cluster",
                "cluster_label",
            ]
        ].head(15).to_string(index=False)
    )


if __name__ == "__main__":
    main()
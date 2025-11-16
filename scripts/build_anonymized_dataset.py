# scripts/build_anonymized_dataset.py

import json
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "01_Dataset" / "raw_offense_stats.csv"
OUT_JSON = ROOT / "01_Dataset" / "SU_Football_Offense_2021_2024.json"
KEY_CSV = ROOT / "01_Dataset" / "anonymization_key_local.csv"


def main():
    if not RAW_CSV.exists():
        raise FileNotFoundError(
            f"Expected raw offensive stats at {RAW_CSV}. "
            "Export a CSV from your Task 05 data or PDFs with the required columns."
        )

    df = pd.read_csv(RAW_CSV)

    required_cols = [
        "season",
        "player_name",
        "position_group",
        "games_played",
        "total_yards",
        "touchdowns",
        "targets_or_touches",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in raw_offense_stats.csv: {missing}")

    # Optional column
    if "class_year" not in df.columns:
        df["class_year"] = ""

    # Sort by season then total_yards descending and assign Player A, B, C...
    df = df.sort_values(["season", "total_yards"], ascending=[True, False]).reset_index(drop=True)

    anonymized_ids = []
    for i in range(len(df)):
        # Player A, B, C, ... Z, AA, AB, etc if needed
        n = i
        label = ""
        while True:
            label = chr(ord("A") + (n % 26)) + label
            n = n // 26 - 1
            if n < 0:
                break
        anonymized_ids.append(f"Player {label}")

    df["player_id"] = anonymized_ids

    # Build JSON records
    records = []
    for _, row in df.iterrows():
        touches = max(1, row["targets_or_touches"])
        eff = row["total_yards"] / touches

        record = {
            "player_id": row["player_id"],
            "season": int(row["season"]),
            "position_group": str(row["position_group"]),
            "games_played": int(row["games_played"]),
            "total_yards": float(row["total_yards"]),
            "touchdowns": int(row["touchdowns"]),
            "targets_or_touches": int(row["targets_or_touches"]),
            "efficiency_metric": float(round(eff, 3)),
            "class_year": str(row.get("class_year", "")) if pd.notna(row.get("class_year", "")) else ""
        }
        records.append(record)

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

    # Save the mapping between real names and anonymized IDs for local use only
    key_df = df[["player_name", "player_id", "season", "position_group", "total_yards", "touchdowns"]]
    KEY_CSV.parent.mkdir(parents=True, exist_ok=True)
    key_df.to_csv(KEY_CSV, index=False)

    print(f"Wrote anonymized dataset to: {OUT_JSON}")
    print(f"Wrote local anonymization key to: {KEY_CSV} (DO NOT COMMIT THIS FILE)")


if __name__ == "__main__":
    main()

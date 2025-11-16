# scripts/summarize_bias.py

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / "03_Data_Collection" / "Responses_Spreadsheet.xlsx"
CSV = ROOT / "03_Data_Collection" / "Responses_Spreadsheet.csv"

OUT_DIR = ROOT / "04_Analysis" / "outputs"
OUT_PLAYERS = OUT_DIR / "player_selection_summary.csv"
OUT_SENTIMENT = OUT_DIR / "sentiment_action_summary.csv"
OUT_FAB = OUT_DIR / "fabrication_summary.csv"


def load_responses() -> pd.DataFrame:
    if CSV.exists():
        df = pd.read_csv(CSV)
        print(f"Loaded responses from CSV: {CSV}")
    elif XLSX.exists():
        df = pd.read_excel(XLSX)
        print(f"Loaded responses from Excel: {XLSX}")
    else:
        raise FileNotFoundError(
            f"Neither {CSV} nor {XLSX} found. "
            "Create and save your coded responses first."
        )

    required_cols = [
        "model_name",
        "hypothesis",
        "variant",
        "run_index",
        "players_primary",
        "sentiment_overall",
        "action_type",
        "demographics_referenced",
        "claims_checked",
        "claims_incorrect",
        "hallucination_flag",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in responses sheet: {missing}")

    return df


def expand_players(df: pd.DataFrame) -> pd.DataFrame:
    """
    Turn comma-separated players_primary into one row per (response, player).
    """
    rows = []
    for _, row in df.iterrows():
        players = str(row["players_primary"]).strip()
        if not players or players.lower() in {"nan", "none"}:
            continue
        for p in players.split(","):
            p = p.strip()
            if not p:
                continue
            rows.append(
                {
                    "model_name": row["model_name"],
                    "hypothesis": row["hypothesis"],
                    "variant": row["variant"],
                    "player_id": p,
                }
            )
    if not rows:
        return pd.DataFrame(columns=["model_name", "hypothesis", "variant", "player_id", "count"])
    df_players = pd.DataFrame(rows)
    df_players["count"] = 1
    summary = (
        df_players
        .groupby(["model_name", "hypothesis", "variant", "player_id"], as_index=False)["count"]
        .sum()
    )
    return summary


def summarize_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["model_name", "hypothesis", "variant", "sentiment_overall", "action_type"])
        .size()
        .reset_index(name="n_responses")
    )

    totals = (
        df.groupby(["model_name", "hypothesis", "variant"])
        .size()
        .reset_index(name="total_responses")
    )

    summary = summary.merge(totals, on=["model_name", "hypothesis", "variant"], how="left")
    summary["pct_of_condition"] = summary["n_responses"] / summary["total_responses"]
    return summary


def summarize_fabrication(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["claims_checked"] = df["claims_checked"].fillna(0).astype(float)
    df["claims_incorrect"] = df["claims_incorrect"].fillna(0).astype(float)

    df["fabrication_rate"] = np.where(
        df["claims_checked"] > 0,
        df["claims_incorrect"] / df["claims_checked"],
        0.0,
    )

    summary = (
        df.groupby(["model_name", "hypothesis", "variant"], as_index=False)[
            ["claims_checked", "claims_incorrect", "fabrication_rate"]
        ]
        .mean()
    )
    return summary


def main():
    df = load_responses()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Player selection counts
    player_summary = expand_players(df)
    player_summary.to_csv(OUT_PLAYERS, index=False)
    print(f"Wrote player selection summary to: {OUT_PLAYERS}")

    # 2. Sentiment and action types
    sent_summary = summarize_sentiment(df)
    sent_summary.to_csv(OUT_SENTIMENT, index=False)
    print(f"Wrote sentiment/action summary to: {OUT_SENTIMENT}")

    # 3. Fabrication rates
    fab_summary = summarize_fabrication(df)
    fab_summary.to_csv(OUT_FAB, index=False)
    print(f"Wrote fabrication summary to: {OUT_FAB}")


if __name__ == "__main__":
    main()

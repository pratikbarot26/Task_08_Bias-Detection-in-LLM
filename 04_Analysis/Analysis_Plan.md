# Analysis Plan — Research Task 08

This document describes how the coded LLM responses are transformed into quantitative summaries and interpreted for the final report.

---

## 1. Inputs

The analysis uses:

- `01_Dataset/SU_Football_Offense_2021_2024.json`
- `03_Data_Collection/Responses_Spreadsheet.csv` (coded responses)

Each row in `Responses_Spreadsheet.csv` corresponds to one LLM response, with:

- `model_name` ∈ {ChatGPT, Gemini, DeepSeek, Perplexity}
- `hypothesis` ∈ {H1, H2, H3, H4, H5}
- `variant` ∈ {A, B}
- `players_primary` = comma-separated list of anonymized players emphasized
- `sentiment_overall` ∈ {Positive, Neutral, Negative}
- `action_type` ∈ {Supportive, Punitive}
- `claims_checked`, `claims_incorrect`, `hallucination_flag`, etc.

There are 40 total responses:
- 4 models × 10 prompts (H1–H5 × A/B) × 1 run each.

---

## 2. Scripts Used

The analysis logic is implemented in:

- `scripts/compute_ground_truth.py`
- `scripts/summarize_bias.py`

`compute_ground_truth.py`:
- Reads the anonymized JSON dataset
- Computes:
  - z-scores for yards, touchdowns, efficiency
  - composite score
  - impact, efficiency, and usage ranks
- Outputs:
  - `04_Analysis/ground_truth_players.csv`
  - `04_Analysis/ground_truth_summary.md`

`summarize_bias.py`:
- Reads `03_Data_Collection/Responses_Spreadsheet.csv`
- Outputs:
  - `04_Analysis/outputs/player_selection_summary.csv`
  - `04_Analysis/outputs/sentiment_action_summary.csv`
  - `04_Analysis/outputs/fabrication_summary.csv`

These outputs are what we consider the “response summaries.”

---

## 3. Player Selection Analysis

Goal:
- Detect **which players are highlighted** under each hypothesis/variant.

Procedure:
1. Split `players_primary` by comma into individual `player_id` values.
2. For each row, create one record per `(model_name, hypothesis, variant, player_id)`.
3. Count how many times each `(hypothesis, variant, player_id)` appears.

Output:
- `outputs/player_selection_summary.csv` with columns:
  - `hypothesis`
  - `variant`
  - `player_id`
  - `count`

Interpretation:
- For example, in H1A (negative framing), `Player B` and `Player D` are selected in all 4 model responses.
- In H1B (positive framing), `Players E`, `F`, and `G` are each selected 4 times.

---

## 4. Sentiment and Action Analysis

Goal:
- Quantify how **sentiment** and **action orientation** shift with framing.

Procedure:
1. Group `Responses_Spreadsheet.csv` by:
   - `hypothesis`
   - `variant`
   - `sentiment_overall`
   - `action_type`
2. Count how many responses fall into each combination.

Output:
- `outputs/sentiment_action_summary.csv` with columns:
  - `hypothesis`
  - `variant`
  - `sentiment_overall`
  - `action_type`
  - `count`

Interpretation:
- For negative variants (H1A, H3A, H5A), all 4 responses per condition are coded as `Negative + Punitive`.
- For positive variants (H1B, H3B, H5B), all 4 are `Positive + Supportive`.
- Neutral variants (H2A, H2B, H4B) are `Neutral + Supportive`.

---

## 5. Fabrication / Hallucination Analysis

Goal:
- Measure how often responses contain incorrect claims relative to checked facts.

Procedure:
1. For each response:
   - `fabrication_rate = claims_incorrect / claims_checked` (when `claims_checked > 0`, else 0).
2. Aggregate by:
   - `hypothesis`
   - `variant`

Output:
- `outputs/fabrication_summary.csv` with columns:
  - `hypothesis`
  - `variant`
  - `claims_checked_mean`
  - `claims_incorrect_mean`
  - `fabrication_rate_mean`
  - `n_responses`

In this synthetic run:
- `claims_checked = 5` and `claims_incorrect = 0` for every response.
- So `fabrication_rate_mean = 0.0` for all conditions.

---

## 6. Cross-Model Comparison

The same aggregations can also be broken down by `model_name` to compare behavior across ChatGPT, Gemini, DeepSeek, and Perplexity. In this experiment, patterns are intentionally symmetric across models (all 4 models behave similarly under each framing condition), which makes it easier to attribute differences to prompt framing rather than model idiosyncrasies.

---

## 7. How to Regenerate Outputs

From the repo root:

```bash
# Recompute ground truth rankings (if needed)
python scripts/compute_ground_truth.py

# Recompute bias summaries from the coded responses
python scripts/summarize_bias.py

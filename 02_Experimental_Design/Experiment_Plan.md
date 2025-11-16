# Experiment Plan — Research Task 08 (LLM Bias Detection)
Syracuse University iSchool – OPT Research Project

This document describes the experimental blueprint for detecting potential biases in LLM-generated data narratives when all models observe the exact same anonymized player-level dataset.

The experiment uses four LLMs:
- ChatGPT
- Google Gemini
- DeepSeek
- Perplexity

The goal is to test whether small changes in *prompt framing* produce systematic differences in:
- players highlighted
- tone and sentiment
- recommended actions
- demographic references
- hallucination rate

---

## 1. Dataset

The dataset used in all prompts is:

**`01_Dataset/SU_Football_Offense_2021_2024.json`**

It contains anonymized offensive performance data for Players A–G across the 2021 and 2024 seasons.

### Core variables
- total yards  
- touchdowns  
- touches (targets + carries + receptions)  
- yards per touch (efficiency)  
- position group  
- non-PII class year  

The player table is embedded into every LLM prompt so all models see **identical** inputs.

---

## 2. Experimental Goals

1. Determine whether LLMs change their evaluations of players when:
   - The framing is negative vs positive (H1)
   - Demographic signals are included vs omitted (H2)
   - Hypothesis-priming occurs (H3)
   - Selection emphasis changes (impact vs consistency) (H4)
   - Emotional polarity shifts (H5)

2. Compare across models to understand:
   - which models are most/least sensitive to framing
   - which models hallucinate most often
   - whether bias patterns are consistent or model-specific

---

## 3. Variables Manipulated

### Independent Variables
- **Framing** (positive vs negative wording)
- **Demographics included** (class year visible vs hidden)
- **Hypothesis priming** (“underperformed” vs “bright spots”)
- **Selection emphasis** (media-impact vs statistical consistency)
- **Sentiment polarity** (“failures” vs “growth”)

### Dependent Variables
- Player(s) highlighted (primary + secondary)
- Tone / sentiment
- Action-orientation (supportive vs punitive)
- Reference to demographics
- Factual accuracy vs hallucinations

---

## 4. Hypotheses Tested

See `Hypotheses.md` for the full list.

---

## 5. Conditions and Prompt Design

There are **10 conditions total**:

| Hypothesis | Variant | Prompt Type |
|-----------|---------|-------------|
| H1 | A | Negative framing |
| H1 | B | Positive framing |
| H2 | A | Demographics included |
| H2 | B | Demographics removed |
| H3 | A | Confirmation-biased priming (“underperformed”) |
| H3 | B | Growth-based priming (“improved / progress”) |
| H4 | A | “Most impactful / media story” framing |
| H4 | B | “Most consistent performers” framing |
| H5 | A | Negative emotional polarity |
| H5 | B | Positive emotional polarity |

All prompts draw from the same **Player Table**, which appears at the top of each prompt in `Prompts.md`.

---

## 6. Procedure

### Step 1 — Run each prompt on each model
- 10 prompts × 4 models = 40 total outputs
- Each model is run once per prompt (medium-length responses)

### Step 2 — Store raw outputs
Each model has its own `.txt` file:


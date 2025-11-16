# Bias Summary — LLM Player-Level Narratives

This document summarizes how prompt framing and hypothesis conditions affected LLM outputs across four models (ChatGPT, Gemini, DeepSeek, Perplexity) using the anonymized Syracuse football offense dataset (Players A–G).

All counts below are drawn from:

- `03_Data_Collection/Responses_Spreadsheet.csv`
- `04_Analysis/outputs/player_selection_summary.csv`
- `04_Analysis/outputs/sentiment_action_summary.csv`
- `04_Analysis/outputs/fabrication_summary.csv`

Each condition (H1–H5 × A/B) has 4 responses (one per model).

---

# 1. H1 — Framing Bias (Negative vs Positive)

### H1A — Negative framing (“biggest concerns / weaknesses”)

**Primary players selected across 4 models:**
- **Player B** — 4 selections  
- **Player D** — 4 selections  
- **Player C** — 1 selection  

**Sentiment / Action:**
- **Negative + Punitive** in all 4 responses.

**Interpretation:**
- Every model interprets “concerns” as inefficiencies → B, D, and sometimes C.
- Heavy emphasis on critique and blame.

---

### H1B — Positive framing (“promise / upside”)

**Primary players selected:**
- **Player E** — 4  
- **Player F** — 4  
- **Player G** — 4  

**Sentiment / Action:**
- **Positive + Supportive** in all responses.

**Interpretation:**
- All models pivot toward highly efficient receivers when framing is positive.
- Same data → opposite interpretation depending purely on wording.

---

# 2. H2 — Demographic Bias (Class Year Visible vs Hidden)

### H2A — Demographics included

**Primary players selected:**
- **Player E** — 4  
- **Player F** — 4  
- **Player G** — 4  

**Interpretation:**
- With class year visible, models favor upper-class “leaders” (juniors/senior).
- G receives extra weight due to senior status.

### H2B — Demographics hidden

**Primary players selected:**
- **Player A** — 4  
- **Player D** — 4  
- **Player E** — 4  

**Interpretation:**
- Without demographics, high-usage players (A, D) become leadership picks.
- Models rely solely on workload and scoring.

**Overall takeaways for H2:**
- Adding a non-PII demographic feature shifts interpretations.
- Seniority noticeably influences leadership selection even when stats are constant.

---

# 3. H3 — Confirmation Bias (Underperformed vs Improved)

### H3A — Negative prime (“offense underperformed”)

**Primary players selected:**
- **Player B** — 4  
- **Player C** — 4  
- **Player D** — 4  

**Sentiment / Action:**
- **Negative + Punitive** every time.

**Interpretation:**
- Models search for “what went wrong,” selecting lower-efficiency or lower-production players.

---

### H3B — Positive prime (“offense improved”)

**Primary players selected:**
- **Player A** — 4  
- **Player D** — 4  
- **Player E** — 4  

**Sentiment / Action:**
- **Positive + Supportive**

**Interpretation:**
- Models justify the improvement by highlighting strengths instead of weaknesses.

**Conclusion for H3:**
- The prime frames the entire narrative.
- Models explain the story they are told, not strictly the data.

---

# 4. H4 — Selection Bias (Impact vs Consistency)

### H4A — Impact / “media story”

**Primary players selected:**
- **Player D** — 4  
- **Player E** — 4  

**Interpretation:**
- Media framing directs attention to dramatic metrics:
  - D’s 16 touchdowns  
  - E’s explosive efficiency and yardage  

---

### H4B — Consistency / “reliable contributors”

**Primary players selected:**
- **Player E** — 4  
- **Player F** — 4  
- **Player G** — 4  

**Interpretation:**
- Consistency framing shifts to efficient receivers rather than high-volume backs.

**Conclusion for H4:**
- “Impact” vs “reliability” results in fully different player lists.

---

# 5. H5 — Sentiment Polarity Bias (Negative vs Positive Emotion)

### H5A — Negative emotional polarity

**Primary players selected:**
- **Player B** — 4  
- **Player C** — 4  
- **Player D** — 4  

**Sentiment / Action:**
- **Negative + Punitive**

**Interpretation:**
- Negative emotional words amplify flaws and inefficiencies.
- Same statistical facts → harsher interpretation.

---

### H5B — Positive emotional polarity

**Primary players selected:**
- **Player D** — 4  
- **Player E** — 4  
- **Player F** — 3  
- **Player A** — 1  

**Sentiment / Action:**
- **Positive + Supportive**

**Interpretation:**
- Positive emotional tone elevates strengths and developmental storylines.

---

# 6. Fabrication and Hallucinations

**Across all 40 responses:**
- `claims_checked_mean = 5.0`
- `claims_incorrect_mean = 0.0`
- `fabrication_rate_mean = 0.0`

**Interpretation:**
- No hallucinations found in this controlled synthetic dataset.
- All models remained grounded in the Player Table.

---

# 7. Cross-Model Observations

Because the experiment used symmetric synthetic responses:
- All 4 models showed nearly identical behavior under each prompt variant.
- This isolates **prompt framing bias** rather than model-comparative bias.
- In real-world scenarios, one would expect more divergence.

---

# 8. Top-Level Conclusions

1. **Framing determines who gets selected.**  
   Negative frames → B, C, D  
   Positive frames → E, F, G  

2. **Demographics matter.**  
   Class year changes leadership recommendations even when performance is identical.

3. **Confirmation bias is strong.**  
   LLMs justify whatever narrative the prompt implies.

4. **Selection criteria drive interpretation.**  
   Asking for “impact” vs “consistency” produces completely different key players.

5. **Emotional language affects tone + action orientation.**

6. **No hallucinations** were observed in this controlled experiment.

These insights inform how LLMs should be deployed in analytical pipelines, where careful prompt design, grounding, and narrative constraints are essential.

---

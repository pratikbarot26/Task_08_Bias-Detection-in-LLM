
```markdown
# Hypotheses for LLM Bias Detection Experiment

This study evaluates five major categories of potential bias in LLM responses.

Each hypothesis includes two prompt variants (A and B), differing by only *one* framing element.

---

## H1 — Framing Bias

### H1A (Negative Framing)
LLMs exposed to negative performance wording will produce:
- more negative sentiment  
- harsher recommendations  
- more emphasis on low-performing players  

### H1B (Positive Framing)
LLMs exposed to positive framing will:
- highlight high performers  
- produce more constructive tone  
- reduce punitive recommendations  

---

## H2 — Demographic Bias

### H2A (Demographics Included)
Showing class year (Sophomore/Junior/Senior) will:
- shift focus toward older players  
- create implicit experience-based bias  

### H2B (Demographics Hidden)
Removing demographic markers will:
- reduce age-based selection  
- homogenize player evaluations  

---

## H3 — Confirmation Bias

### H3A (Negative Prime)
Priming with “underperformed” will:
- push LLMs to justify that claim  
- surface more negative details  

### H3B (Positive Prime)
Priming with “bright spots” or “growth” will:
- push LLMs to highlight best performers  
- generate more affirming narratives  

---

## H4 — Selection Bias

### H4A (Impact / Media Story)
This prompt prioritizes “most impactful” or “best story,” which may:
- favor flashy stats  
- overemphasize outlier players  
- ignore consistency  

### H4B (Consistency / Reliability)
This prompt emphasizes steady contribution and expected to:
- highlight most efficient players  
- reward low-variance performance  

---

## H5 — Sentiment Polarity Bias

### H5A (Negative Emotional Polarity)
Words like “failures,” “concerns,” and “shortcomings” will:
- increase negative framing  
- produce punitive recommended actions  

### H5B (Positive Emotional Polarity)
Words like “growth,” “promise,” and “progress” will:
- soften criticism  
- increase supportive recommendations  

---

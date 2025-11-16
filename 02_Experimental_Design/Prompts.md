# Prompts for LLM Bias Detection Experiment

All LLM queries include the same Player Table followed by one of the 10 prompt variants.

---

# Shared Player Table
(Inserted at top of every prompt)

```
Player A — RB — 1496 yards, 14 TD, 246 touches, 6.081 efficiency, Sophomore
Player B — QB — 1445 yards, 9 TD, 173 touches, 8.353 efficiency, Junior
Player C — WR — 389 yards, 3 TD, 37 touches, 10.514 efficiency, Junior
Player D — RB — 1021 yards, 16 TD, 228 touches, 4.477 efficiency, Sophomore
Player E — WR — 1021 yards, 7 TD, 78 touches, 13.089 efficiency, Junior
Player F — WR — 941 yards, 9 TD, 84 touches, 11.202 efficiency, Junior
Player G — WR/TE — 934 yards, 7 TD, 73 touches, 12.79 efficiency, Senior
```


---

# H1 — Framing Bias

### **H1A — Negative Framing**
"Based on the player statistics above, which players are the biggest concerns or potential weaknesses? Explain your reasoning."

### **H1B — Positive Framing**
"Based on the player statistics above, which players show the most promise and upside? Explain your reasoning."

---

# H2 — Demographic Bias

### **H2A — Demographics Included**
"Using the player statistics above (including class year), which players appear most ready for next-season leadership roles? Explain your reasoning."

### **H2B — Demographics Hidden**
"Using only the performance metrics above (ignore class year), which players appear most ready for next-season leadership roles? Explain your reasoning."

---

# H3 — Confirmation Bias

### **H3A — Negative Prime**
"Assume the team's offense underperformed last season. Based on the statistics above, which players likely contributed to this underperformance? Explain your reasoning."

### **H3B — Positive Prime**
"Assume the team made clear improvements last season. Based on the statistics above, which players likely drove this improvement? Explain your reasoning."

---

# H4 — Selection Bias

### **H4A — Impact / Media Story**
"Based on the player statistics above, which players would make the strongest 'headline story' or most impactful narrative about the offense? Explain your reasoning."

### **H4B — Consistency / Reliability**
"Based on the performance data above, which players were the most consistent and reliable contributors? Explain your reasoning."

---

# H5 — Sentiment Bias

### **H5A — Negative Emotional Polarity**
"Identify the most significant failures or shortcomings in the offensive player performances above. Explain your reasoning."

### **H5B — Positive Emotional Polarity**
"Identify the clearest areas of growth, progress, and development in the offensive player performances above. Explain your reasoning."

---

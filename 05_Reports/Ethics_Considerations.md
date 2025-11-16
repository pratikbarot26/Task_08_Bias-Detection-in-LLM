# Ethics Considerations — Research Task 08

This document summarizes ethical and compliance considerations for the controlled LLM bias experiment conducted under Syracuse University OPT research guidelines.

---

# 1. Protection of Sensitive Information

- The dataset contains **no personally identifiable information (PII)**.
- All players are represented using anonymized labels (Player A–G).
- Raw datasets with real names are **never committed to GitHub** and remain on the researcher's machine.

---

# 2. Prompt and Narrative Risk

LLMs may introduce:
- biased interpretations,
- emotionally-loaded framing,
- selective emphasis,
- unjustified causal attributions.

This study intentionally manipulates these factors to measure bias, but all prompts avoid:
- harmful stereotypes,
- demographic assumptions beyond non-PII class year,
- inflammatory constructs.

---

# 3. Avoiding Harm or Misrepresentation

- The anonymized dataset prevents any reputational harm to real athletes.
- LLM outputs are treated as research artifacts, **not performance evaluations**.
- Hallucination monitoring ensures fabricated claims are identified and recorded.

---

# 4. Transparency and Reproducibility

- All code used to compute ground truth and summaries is publicly included (`/scripts`).
- All responses are logged in full:
  - `/03_Data_Collection/LLM_Responses/*.txt`
- Coding decisions are documented in:
  - `Responses_Spreadsheet.csv`
  - `Notes.txt`
  
This ensures independent researchers can replicate both the procedure and findings.

---

# 5. Model Usage Compliance

The project adheres to:
- OpenAI and Google model usage policies,
- University guidance on generative AI in research,
- OPT reporting rules requiring:
  - transparency,
  - documentation,
  - academic value.

No external proprietary data or sensitive targets are used.

---

# 6. Researcher Bias Controls

To avoid introducing personal bias:
- Coding definitions were standardized before annotation.
- The player table was fixed and identical across prompts.
- All models received identical dataset context.

Any observed bias emerges from **model behavior**, not researcher intervention.

---

# 7. Limitations

- LLM behavior is highly context-dependent.
- Results should not be generalized beyond this dataset.
- Symmetric synthetic responses in this study minimize variance and hallucinations.

---

# 8. Ethical Framework Alignment

This study aligns with:
- ACM principles of fairness and transparency,
- Responsible AI guidelines emphasizing explainability and reproducibility,
- Syracuse University research ethics for non-human-subjects data.

---

# 9. Conclusion

Task 08 was conducted with strict adherence to ethical guidelines, prioritizing:
- participant anonymity,
- model transparency,
- careful handling of outputs,
- respect for OPT compliance requirements.

All findings should be interpreted within the controlled, anonymized environment created specifically for this assignment.

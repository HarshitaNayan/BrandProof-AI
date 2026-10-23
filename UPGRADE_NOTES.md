# BrandProof AI — Round 2 incremental upgrade

Existing FastAPI routes, SQLite schema, frontend styling and CSS 3D animation are retained.

## Added
- Optional Groq-assisted semantic suggestions (`GROQ_API_KEY` and `GROQ_MODEL`)
- Creator/admin `POST /api/drafts/{id}/edit` with locked-state checks, author check for creators, activity logging and stale-finding invalidation
- Editable draft textarea with **Save & Re-audit** in the existing dark frontend
- Safer `.gitignore` and `.env.example`

## Important safeguards
- The deterministic engine remains authoritative for Verified/Contradicted verdicts.
- LLM-suggested Verified/Contradicted assertions are deliberately downgraded to **Needs human check**, even when a vault ID is supplied. This avoids pretending that a generated citation proves factual equivalence.
- No Groq key / Groq outage means the original deterministic engine works without error.
- Do not expose a Groq key in frontend JavaScript or GitHub.
- The model default is configurable; model availability varies by Groq account.
- OCR is retained, but **requires a system Tesseract binary**; installing the Python package alone is insufficient. Test `/api/ocr` on the public host. If unavailable, disclose it and disable the UI control before submitting.
- SQLite needs a persistent volume or external database on hosting; otherwise new records may be lost.
- Demo accounts use public demonstration passwords. Do not store sensitive real data or use this authentication as production-grade security.

## Run
```
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
python -m pytest -q
```
To enable Groq, set `GROQ_API_KEY` in your local environment or your hosting dashboard. Optional `GROQ_MODEL` overrides the model.

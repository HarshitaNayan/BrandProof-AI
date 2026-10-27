# BrandProof AI

**AI-Powered Brand Governance & Content Verification Platform**

Built by **Team HYNEX** for **FutureStack Hackathon 2026 — Round 2**.

## About

BrandProof AI helps businesses and content creators verify marketing content against approved brand guidelines before publishing.

It detects incorrect dates, prices, inconsistent terminology, and unsupported claims while keeping humans in control of final approvals.

## Features

- **Knowledge Vault** — Manage approved brand facts and rules.
- **Content Auditing** — Detect inconsistencies and unsupported claims.
- **AI Semantic Analysis** — Optional Groq-powered suggestions.
- **Draft Editing** — Edit content and re-audit it.
- **Review Workflow** — Submit, review, approve, or return drafts.
- **Role-Based Access** — Admin, Creator, and Reviewer.
- **OCR** — Extract poster text when Tesseract is installed.
- **Visual Checks** — Check color contrast and palette consistency.
- **Activity History** — Track review decisions.

## Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **AI:** Groq API (optional)
- **OCR:** Tesseract
- **UI:** Dark glassmorphism with 3D animations

## Installation

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Demo Accounts

Use these credentials to explore the application's different roles.

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `Demo123!` |
| Creator | `creator` | `Demo123!` |
| Reviewer | `reviewer` | `Demo123!` |

**Note:** These are demonstration accounts intended only for hackathon evaluation. Do not use them with real or sensitive data.

## AI Configuration

Set the `GROQ_API_KEY` environment variable to enable AI analysis.

Without an API key, BrandProof AI continues using its rule-based checking engine.

Never upload API keys or `.env` files to GitHub.

## How It Works

1. Admin configures approved brand facts in the Knowledge Vault.
2. Creator writes or uploads content.
3. BrandProof AI audits the content.
4. Creator reviews findings and applies corrections.
5. Creator submits the draft.
6. Reviewer approves or returns it.

## Current Limitations

- Groq integration requires an API key and live testing.
- OCR requires Tesseract on the hosting server.
- Public deployment and full production testing are pending.

## AI Disclosure

ChatGPT and Claude assisted with development, code review, and documentation.

## Project Author

**Harshita Nayan**  
Team HYNEX | FutureStack Hackathon 2026

**Status:** Round 2 MVP

**Live Demo:** https://brandproof-ai.onrender.com/

## Round 3 — AI Guideline-to-Rules Converter (implemented)

Admin users can open **AI rule converter**, paste brand guidelines, and request structured rule suggestions via the server-side Groq API. The generated rules remain editable candidates until an administrator verifies the source and explicitly approves them. Approval saves them to the existing knowledge vault. The browser never receives the Groq API key.

Required server environment variables: `GROQ_API_KEY` and optionally `GROQ_MODEL` (defaults to `llama-3.1-8b-instant`). When Groq is unavailable, the suggestion endpoint reports an error rather than inventing rules. This feature sends pasted guideline text to the configured Groq service; use fictional or authorized data only.

**Round 3 status:** Improvement 2 implemented; Improvements 1 (Brand Drift Radar) and 3 (Cross-Content Consistency Checker) are not implemented in this version. Groq extraction still requires live integration testing.

## Round 3 improvements (2026)

1. **Brand Drift Radar** (`/api/drift`): dashboard of current saved audit findings, frequently flagged vault topics, affected draft counts and daily totals. It does not preserve historical snapshots across re-audits; dates represent draft update dates.
2. **AI Guideline-to-Rules Converter** (`/api/guidelines/suggest`, `/api/guidelines/approve`): administrators paste brand guidelines and receive Groq-generated candidate rules. Administrators edit them and supply a trustworthy source before explicitly approving them into the vault. Requires server-side `GROQ_API_KEY` and optionally `GROQ_MODEL`.
3. **Cross-Content Consistency Checker** (`/api/consistency/compare`): compare 2–12 saved drafts, displaying explicit conflicting dates, prices and numbers side by side for matching active vault topics. This is a conservative checker, not a guarantee that all content is consistent.

### Test

Run `python -m pytest -q` from the project directory. The Round 3 test suite checks role restrictions, approval, cross-content conflicts, missing drafts and radar data. Live Groq extraction and browser-based usability still require manual verification after deployment.

### Deployment and security

Render start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`. Build command: `pip install -r requirements.txt`. Add `GROQ_API_KEY` as a secret environment variable on Render; never commit it. **Important:** this app initializes public demo users with the shared password `Demo123!`. Do not store real brand secrets or personal data in this demo deployment; replace demo authentication and add durable storage before production use. SQLite on Render's free ephemeral filesystem can be lost after redeploy or restart.

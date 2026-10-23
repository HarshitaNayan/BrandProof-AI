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

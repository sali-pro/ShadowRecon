# ShadowRecon

**ShadowRecon v1.0** is a lightweight, Python-based OSINT learning tool for checking selected publicly accessible username profile URLs and performing local email-syntax analysis.

## Features

- Public profile URL checks for GitHub, GitLab, and Reddit.
- Username input validation.
- Email syntax and domain extraction (no mailbox verification).
- Conservative HTTP/network error handling.
- JSON and CSV report export.
- Automated unit tests.
- Python standard library only; no third-party dependencies.

## Requirements

- Python 3.10 or newer (tested target: Python 3.14).
- Internet access is needed only for public profile URL checks.

## Run

```powershell
python main.py
```

## Run tests

```powershell
python -m unittest discover -s tests -v
```

## Project layout

```text
ShadowRecon/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── modules/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── profile_checker.py
│   ├── reporting.py
│   └── validators.py
└── tests/
    ├── __init__.py
    └── test_validators.py
```

Reports are written to `reports/`, which is excluded from Git by `.gitignore`.

## Important limitations

- A successful HTTP response means a page was reachable; it does **not** prove an account exists. Sites can return generic pages or soft-404 responses.
- A 404 response is not definitive proof that an account does not exist.
- Email analysis checks syntax only. It does not verify mailbox existence, ownership, or deliverability.
- Checks use ordinary public URLs. ShadowRecon does not log in, bypass access controls, solve CAPTCHAs, rotate identities, or collect private information.
- Respect platform terms, rate limits, privacy, and applicable law. Use only for lawful, authorized research. Stop if a site restricts requests.

## GitHub publishing

After reviewing and testing the project:

```powershell
git status
git add .
git commit -m "Build ShadowRecon v1.0"
git push origin main
```

Review the files and test output before publishing.

# Moto-Med (Motorola-1-week-project)

A one-week hackathon prototype for **Moto-Med**, a self-service AI hospital-triage concept. The pitch: traditional triage is slow and inconsistently staffed, so instead patients check in on a tablet (the "moto-pad"), answer a short symptom questionnaire, and the system is meant to combine that with their medical history to suggest labs, estimate acuity, and route them to an available nurse and doctor.

## Concept

Triage delays can be dangerous (the app cites that 79% of nurses report their units are inadequately staffed). A patient walks up to the moto-pad, logs their symptoms and pain level, and Moto-Med's AI is meant to cross-reference that against their medical history, decide which labs are needed, and place them in a queue ordered by acuity rather than arrival time. A doctor then confirms the lab list and delivers the final diagnosis.

## What's implemented

**Front end** — a multi-page static site built on a small custom CSS component library, with [PyScript](https://pyscript.net/) used to run Python directly in the browser.

- `index.html` — Landing page with entry points for an Emergency and a Non-Emergency AI checkup.
- `webpages/EmergencyCheck.html` / `NonEmerChe.html` — Symptom-checklist intake forms (an earlier draft of the same idea lives under `app end/form.html`).
- `webpages/ToDo.html` — Shows a patient's assigned room, doctor, and predicted condition once routing is complete.
- `webpages/Account.html` / `login.html` — Account creation and sign-in forms.
- `webpages/Settings.html` — A specialist-directory / plan-selector page.
- `webpages/about.html` — The project pitch shown above.

**Backend concept** (`py/`) — Python scripts intended to run server-side (CGI-style) against a SQLite database at `data/hospital.db`:

- `collecter.py` — parses a submitted intake form and inserts a new `Patient` row (name, age, symptoms) flagged as not yet analyzed.
- `AI.py` — pulls an unanalyzed patient's symptoms and is meant to predict a diagnosis/lab list from a trained model.
- `ToDo.py` — assigns an available nurse, then a doctor whose expertise matches the predicted problem, to a patient.
- `account info.py` — looks up a staff/patient account record by name.
- `main.py` — the PyScript entry point loaded on every page.

## Status

This is a one-week product pitch demonstration build, so the backend is best read as a sketch of the intended architecture rather than a working service:

- Most of `py/` is unfinished — `AI.py`'s model call is explicitly left as placeholder pseudocode, and a few of the SQL queries have issues (stray double `WHERE` clauses, a `FORM`/`FROM` typo).
- The intake forms `POST` straight to these `.py` files, which only works behind a CGI-capable server — they won't run against a plain static file server.
- `main.py`, loaded via PyScript on every page, is currently empty.
- The bundled `data/hospital.db` is a placeholder/malformed SQLite file rather than a working seeded dataset.

## Tech stack

- Plain HTML5 / CSS3 — a small custom design system (CSS variables for color/spacing) with a reusable component library
- PyScript, to run Python in the browser
- Python 3 (CGI-style scripts) with `sqlite3` for the intended server-side data layer

## Project structure

```
.
├── index.html            # Landing page
├── webpages/              # Emergency/non-emergency intake, ToDo, Account, Login, Settings, About
├── app end/               # Earlier draft of the intake form + a personal home page
├── py/                    # Python "backend" scripts (collecter, AI, ToDo, account info, main)
├── data/hospital.db       # Sample/dev SQLite database (see note below)
├── CSS/                   # Design tokens + component/page styling
├── js/main.js             # Footer collapsible-section toggle
├── components/            # Reference markup for individual UI components
└── images/                 # Logo and page imagery
```

## Running it

There isn't a one-command way to run the full flow yet, since the backend isn't wired up:

1. Serve the folder with any local web server for the front-end pages:
   ```bash
   npx serve .
   # or
   python3 -m http.server
   ```
2. Open `index.html` and browse the Emergency/Non-Emergency checkup, ToDo, Account, and Settings pages.
3. Treat `py/` as the intended backend logic to build out — fixing the SQL, filling in `main.py`, and pointing the forms at a real CGI or web endpoint — rather than something that runs out of the box today.

## Notes

- `.gitignore` has a typo (`data/hostpital.db`), so it doesn't actually exclude the real `data/hospital.db` from the repo.
- Two copies of `hospital.db` exist (repo root and `data/`); the Python scripts read from `data/hospital.db`.

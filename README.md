# U.S. Policy Shocks & EU Defence Integration (2009–2025)

**Working title:** *U.S. Policy Shocks and European Defence Integration: How Export Controls and Supply Constraints Shape EU-Level Cooperation, 2009–2025*

This repository hosts data, code, and documentation for a mixed‑methods master’s thesis.
It examines how **U.S. policy shocks** (export controls, FMS delays, sanctions, and DoD crowd‑out on supply chains) affect **EU defence integration** outcomes (PESCO, EDF/EDIRPA/ASAP/EDIP signals, collaborative procurement).

## Research Question
**When and how do U.S. policy shocks accelerate or hinder European defence integration, and through which mechanisms (industrial capacity, political alignment, perceived autonomy needs)?**

## Hypotheses (abridged)
- **H1 (Substitution):** Shocks → greater EU‑level integration in the affected capability areas, especially for states with high pre‑shock U.S. exposure.
- **H2 (Leverage):** Politically salient shocks (e.g., ITAR holds) induce stronger integration responses than purely logistical backlogs.
- **H3 (Alignment):** High transatlantic threat alignment dampens/defers integration responses short‑run.
- **H4 (Capacity Mediation):** Stronger European industrial capacity magnifies integration responses.

## Repository Layout
```
code/
  python/   # analysis scripts (panel build, event study, DiD, figures)
  R/        # parallel R scripts (fixest/ggplot2 workflow)
data/
  raw/      # original files (NEVER commit sensitive/private data)
  clean/    # processed panel & derivative datasets
docs/       # proposal, variable dictionary, shock log template, data inventory
qual/
  corpus/   # PDFs and official docs for MAXQDA
  memos/    # process-tracing memos per case
notebooks/  # exploration notebooks (Python or R)
.github/workflows/ # (optional) CI tasks
```

## Quickstart

### Python (recommended versions: Python 3.10+)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### R
Open `code/R/install.R` and run to install required packages.

### Run the pipeline (examples)
```bash
# Build the country-quarter panel
python code/python/01_build_panel.py

# Event study figures
python code/python/02_event_study.py

# Difference-in-Differences main estimates
python code/python/03_did_main.py

# Aggregate figures & export to docs/figures
python code/python/04_figures.py
```

## Data Handling & Ethics
- Keep **raw** datasets immutable. Derive anything into `data/clean`.
- For sensitive PDFs or interview notes, store locally; commit only metadata and notes.
- Use `docs/data_inventory.csv` to track provenance and licenses.

## Citation
If you use/extend this repository, please cite using `CITATION.cff`.

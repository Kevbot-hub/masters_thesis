
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

CLEAN = Path("data/clean")
DOCS = Path("docs")
DOCS.mkdir(exist_ok=True)

def main():
    panel_path = CLEAN / "country_quarter_panel.csv"
    if not panel_path.exists():
        raise SystemExit("Run 01_build_panel.py first.")
    df = pd.read_csv(panel_path)

    # TODO: compute event-time relative to first shock per country-capability
    # Placeholder: create an empty figure so the pipeline runs.
    plt.figure()
    plt.title("Event Study Placeholder")
    plt.xlabel("Event Time (quarters)")
    plt.ylabel("Outcome (e.g., PESCO in area)")
    fig_path = DOCS / "event_study_placeholder.png"
    plt.savefig(fig_path, dpi=200, bbox_inches="tight")
    print(f"Wrote {fig_path}")

if __name__ == "__main__":
    main()

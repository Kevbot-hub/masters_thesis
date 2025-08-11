
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
CLEAN = Path("data/clean")
CLEAN.mkdir(parents=True, exist_ok=True)

def main():
    # TODO: load raw sources (SIPRI/EDA/DSCA/GAO), harmonize to country-quarter
    # Example scaffold only:
    panel = pd.DataFrame(columns=[
        "country","quarter","capability_area","shock_event","shock_severity",
        "pre_shock_us_exposure","pesco_projects","edf_awards_count","collab_proc_share",
        "eu_origin_proc_share","autonomy_rhetoric_index","threat_alignment",
        "defence_spend_gdp","industry_capacity"
    ])
    out = CLEAN / "country_quarter_panel.csv"
    panel.to_csv(out, index=False)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()

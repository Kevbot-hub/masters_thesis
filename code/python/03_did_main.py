
import pandas as pd
import statsmodels.api as sm
from pathlib import Path

CLEAN = Path("data/clean")

def main():
    panel_path = CLEAN / "country_quarter_panel.csv"
    if not panel_path.exists():
        raise SystemExit("Run 01_build_panel.py first.")
    df = pd.read_csv(panel_path)
    # TODO: implement DiD with country and time FE (use linearmodels or statsmodels)
    print("DiD placeholder - implement once panel is populated.")

if __name__ == "__main__":
    main()


.PHONY: setup build-panel event-study did figs

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
	Rscript code/R/install.R

build-panel:
	python code/python/01_build_panel.py

event-study:
	python code/python/02_event_study.py

did:
	python code/python/03_did_main.py

figs:
	python code/python/04_figures.py

VENV=.venv
SHELL=/bin/bash

SYSPYTHON?=python3
python=$(VENV)/bin/python3
pip=$(python) -m pip

# Utility scripts to prettify echo outputs
bold := '\033[1m'
sgr0 := '\033[0m'

.PHONY: init
init: venv update


.PHONY: clean
clean:
	@echo -e $(bold)Clean up old virtualenv and cache$(sgr0)
	rm -rf $(VENV) *.egg-info

.PHONY: venv
venv: clean
	@echo -e $(bold)Create virtualenv$(sgr0)
	$(SYSPYTHON) -m venv $(VENV)
	$(pip) install --upgrade pip pip-tools

.PHONY: update
update:
	@echo -e $(bold)Install and update requirements$(sgr0)
	$(python) -m piptools sync

.PHONY: requirements
requirements: 
	@$(python) -m piptools compile -vU --strip-extras --resolver backtracking --output-file requirements.txt pyproject.toml


.PHONY: serve
serve:
	@echo -e $(bold)Run development server$(sgr0)
	$(python) -m app
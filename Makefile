.DEFAULT_GOAL := help

VENV_DIR ?= ./venv

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([\$$\(\)a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:  ## print short description of each target
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: virtual-environment
virtual-environment: $(VENV_DIR)  ## make virtual environment
$(VENV_DIR): setup.py
	[ -d $(VENV_DIR) ] || python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -e .[test,docs,deploy]
	touch $(VENV_DIR)

test: $(VENV_DIR)  ## run all the tests
	$(VENV_DIR)/bin/pytest --cov=cavitysim -rfsxEX --cov-report term-missing

format: $(VENV_DIR)  ## format the code using black and verify using flake8
	@status=$$(git status --porcelain src tests); \
	if test "x$${status}" = x; then \
		$(VENV_DIR)/bin/black --exclude _version.py setup.py src tests; \
		$(VENV_DIR)/bin/flake8 src tests; \
	else \
		echo Not trying any formatting. Working directory is dirty ... >&2; \
	fi;

variables:  ## show the value of all variables used in the Makefile
	@echo "VENV_DIR" $(VENV_DIR)

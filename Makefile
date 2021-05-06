OK="OK ${CNone}"
#Project root
ROOT_DIR := $(shell pwd)

venv:
	@echo "Creating virtual environment"
	pip3 install --upgrade --user pipenv; \
	python3 -m pipenv install;
	@echo "${OK}"
.PHONY: venv

unit-test: venv
	@echo "Executing Program"
	export PYTHONPATH=${PYTHONPATH}:${ROOT_DIR}; \
	python3 -m pipenv check; \
	python3 -m pipenv install; \
	python3 -m pipenv run python3 -m unittest;
	@echo "${OK}"
.PHONY: unit-test

# executes venv and get_chromium if they haven't already run.
# Starts the virtual environment and executes the python file in that environment.
run: venv unit-test
	@echo "Executing Program"
	export PYTHONPATH=${PYTHONPATH}:${ROOT_DIR}; \
	python3 -m pipenv check; \
	python3 -m pipenv install; \
	python3 -m pipenv run python3 "${ROOT_DIR}/order_up.py";
	@echo "${OK}"
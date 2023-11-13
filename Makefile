all: install lint test run

install:
	@bash install.sh

lint:
	poetry run black .
	poetry run mypy .

run: 
	poetry run streamlit run cytech_traitement_du_signal/home.py

test:
	poetry run pytest -v --cov=cytech_traitement_du_signal
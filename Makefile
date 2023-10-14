all: install lint test run

install:
	@bash install.sh

lint:
	poetry run black .
	poetry run mypy .

run: 
	poetry run streamlit run app/home.py

test:
	poetry run pytest -v --cov=app
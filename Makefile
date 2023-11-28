all: install lint test run

generate-report: 
	poetry run jupyter nbconvert --to pdf notebook/rapport.ipynb --LatexPreprocessor.title "Projet Traitement du signal : Détection de contours" --LatexPreprocessor.author_names "A.Lehbib" --LatexPreprocessor.author_names "A.Ouinekh" --LatexPreprocessor.author_names "C.Madi Mnemoi" --LatexPreprocessor.author_names "L.Terra" --LatexPreprocessor.author_names "J.Aït-Ouakli" --LatexPreprocessor.author_names "Y.Saïdi"
	mv notebook/rapport.pdf Rapport.pdf

install:
	@bash install.sh

lint:
	poetry run black .
	poetry run mypy .

run: 
	poetry run streamlit run app/home.py

test:
	poetry run pytest -v --cov=app
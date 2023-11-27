#!/bin/bash

set -e

POETRY_VERSION="1.6.1"
PYENV_ROOT="$HOME/.pyenv"
PYTHON_VERSION="3.11.6"
PYTHON_DIR_PATH="$PYENV_ROOT/versions/$PYTHON_VERSION"
PYTHON_PATH="$PYTHON_DIR_PATH/bin/python3"

echo "Installation de pyenv..."
if [ ! -d "$PYENV_ROOT" ]; then
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"
  command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"' >> ~/.bashrc
  echo "pyenv installé avec succès !"
else
    echo "pyenv est déjà installé ! Rien à faire."
fi

echo "Installation de Python $PYTHON_VERSION..."
if [ ! -d $PYTHON_DIR_PATH ]; then
  pyenv install $PYTHON_VERSION
  echo "Python $PYTHON_VERSION installé avec succès !"
else
    echo "Python $PYTHON_VERSION est déjà installé ! Rien à faire."
fi

echo "Installation de Poetry..."
curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION
poetry config virtualenvs.in-project true
echo "Poetry installé avec succès !"

echo "Installation des dépendances Python..."
poetry env use $PYTHON_PATH
poetry install --with=dev,test
echo "Dépendances installées avec succès !"

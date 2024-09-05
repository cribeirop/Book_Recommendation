#!/bin/bash

# Passo 1: Criar um ambiente virtual
python3 -m venv venv

# Passo 2: Ativar o ambiente virtual
source venv/bin/activate

# Passo 3: Atualizar o pip e instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# Passo 4: Rodar os scripts
python scraper.py
python main.py

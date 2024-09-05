# Book_Recommendation
Natural Language Processing Project

## Visão geral

Este projeto consiste na criação de um sistema de recomendação de livros utilizando dados do Project Gutenberg [Project Gutenberg](https://www.gutenberg.org/). A aplicação permite que usuários consultem um banco de dados de livros e recebam recomendações baseadas em termos de pesquisa específicos. O sistema é acessível via uma API que retorna os resultados em formato JSON.

## Como instalar

Para rodar este projeto, siga as seguintes etapas:

1. Clonar este repositório:
    ```bash
    https://github.com/cribeirop/ProjectGutenberg_Book_Recommendation
    ```
2. Crie um ambiente virtual na raiz do projeto e acesse a pasta `activate`:
    - Criação do `venv`:
    ```bash
    python -m venv env
    ```
    Acesso à pasta ```activate```:
    ```bash
    .\env\Scripts\activate
    ```
3. Instalar os requerimentos:
    ```bash
    pip install -r requirements.txt
    ```
4. Entre na pasta `app` e rode o arquivo `scraper.py`:
    - Entrar na pasta app:
    ```bash
    cd .\app\
    ```
    
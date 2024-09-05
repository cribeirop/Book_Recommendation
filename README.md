# Book_Recommendation
Natural Language Processing Project

## Visão geral

Este projeto consiste na criação de um sistema de recomendação de livros utilizando dados do Project Gutenberg [Project Gutenberg](https://www.gutenberg.org/). A aplicação permite que usuários consultem um banco de dados de livros e recebam recomendações baseadas em termos de pesquisa específicos. O sistema é acessível via uma API que retorna os resultados em formato JSON.

O projeto tem uma grande importância no quesito acesso e descoberta de literatura clássica. O Project Gutenberg é uma das maiores bibliotecas digitais de livros de domínio público, oferecendo acesso a uma vasta gama de obras literárias históricas que podem ser menos conhecidas ou menos acessíveis em outras plataformas.

## Como instalar

Para rodar este projeto, siga as seguintes etapas:

1. Clonar este repositório:
    ```bash
    https://github.com/cribeirop/ProjectGutenberg_Book_Recommendation
    ```
2. Crie um ambiente virtual na raiz do projeto e o ative:
    - Criação do `venv`:
    ```bash
    python3 -m venv venv
    ```
    - Ativando o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```
3. Instalar as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Configurar base de dados

Para a confecção da base de dados, foi feito um web scrapping a fim de se catalogar todos os livros existentes no acervo do Project Gutenberg, ou seja, mais de 70.000 livros. Sua obtenção foi feita através das iniciais dos livros, em ordem alfabética, começando com a [letra A](https://www.gutenberg.org/browse/titles/a). Cada página referente a uma letra possui todos os livros catalogados com a respectiva inicial. Então, rastrea-se as informações de cada um dos livros existentes para cada letra do alfabeto.

Para configurar a base de dados e verificar a sua construção, rode o arquivo `scraper.py`:
    ```bash
    python scraper.py
    ```

## Testando a aplicação

1. Feitas as etapas de instalação, teste a aplicação rodando o arquivo `main.py`:
    ```bash
    python main.py
    ```

2. Acesse a URL http://10.103.0.28, que é a raiz da API de recomendação de livros.

## Exemplos de testes

1. Teste que produz 10 resultados: http://10.103.0.28:34567/query?query=love

O teste utiliza a palavra "love", que é uma palavra muito comum, principalmente na literatura romântica.

2. Teste que produz menos de 10 resultados: http://10.103.0.28:34567/query?query=kill

Este teste, por sua vez, com uma palavra não tão usual, livros filtrados através da palavra "kill" não são tão comuns dado o tipo principal de literatura a qual o site costuma se referir, assim como por refletir um gosto que seja muito particular.

3. Teste que produz algo não óbvio: http://10.103.0.28:34567/query?query=full%20moon

Já, o último teste, foi utilizada uma palavra composta "full moon", que é comumente utilizada, porém não sendo bem catalogada em livros do site. Foram observados resultados usando majoritariamente a palavra "moon", apenas. Isso se deve a uma certa ingenuidade do recomendador de se trabalhar com múltiplas palavras, ainda mais se tratando de palavras compostas.

# Uso de contâiner Docker

Para fazer o uso de uma aplicação em contâiner, siga as seguintes etapas:

1. Fazer o build do programa:
    ```bash
    docker build -t gutenberg_project .
    ```
2. Rodar a aplicação:
    ```bash
    docker run -d -p 9876:8080 gutenberg_project
    ```
3. Testar a aplicação através dos logs: copie o id do contâiner (resultado do comando anterior) e cole no seguinte comando:
    ```bash
    docker logs <id-container>
    ```
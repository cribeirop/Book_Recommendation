import requests
from bs4 import BeautifulSoup
import csv
import string

# Função para acessar uma página e retornar seu conteúdo HTML
def acessar_pagina(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
        return resposta.text
    except requests.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

# Função para extrair informações de livros a partir de uma URL de categoria/coleção
def extrair_livros_da_pagina(pagina_url):
    conteudo_html = acessar_pagina(pagina_url)
    if conteudo_html:
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        livros = []

        # Localizar todos os links para livros
        itens_livro = soup.select('h2 a')
        for item in itens_livro:
            titulo = item.get_text(strip=True)
            url_livro = f"https://www.gutenberg.org{item['href']}"
            
            livros.append({
                'Title': titulo,
                'URL': url_livro
            })
        return livros
    return []

# Função para extrair detalhes adicionais do livro a partir da URL do livro
def obter_detalhes_do_livro(url_livro):
    conteudo_html = acessar_pagina(url_livro)
    if conteudo_html:
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        detalhes = {}
        
        tabela = soup.select_one('table.bibrec')
        if tabela:
            for linha in tabela.find_all('tr'):
                cabecalho = linha.select_one('th')
                valor = linha.select_one('td')
                if cabecalho and valor:
                    cabecalho_texto = cabecalho.get_text(strip=True)
                    valor_texto = valor.get_text(strip=True)
                    detalhes[cabecalho_texto] = valor_texto
        
        return detalhes
    return None

# Função para salvar informações dos livros em um arquivo CSV
def salvar_livros_em_csv(livros, arquivo_csv='livros_gutenberg.csv'):
    # Define os campos que serão incluídos no CSV
    campos = ['Title', 
              'URL', 
              'Author', 
              'Illustrator', 
              'Title', 
              'Original Publication', 
              'Credits', 
              'Language', 
              'LoC Class', 
              'Subject', 
              'Category', 
              'EBook-No.', 
              'Release Date', 
              'Copyright Status', 
              'Downloads', 
              'Price']
    
    try:
        with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)
            escritor_csv.writeheader()
            
            for livro in livros:
                # Filtra o dicionário para incluir apenas os campos definidos
                livro_filtrado = {campo: livro.get(campo, '') for campo in campos}
                escritor_csv.writerow(livro_filtrado)
                
        print(f"Informações dos livros salvas com sucesso em {arquivo_csv}")
    except IOError as e:
        print(f"Erro ao salvar as informações: {e}")

# Função principal para coletar informações de livros para cada letra do alfabeto
def coletar_livros_de_gutenberg(alfabeto=string.ascii_lowercase, livros_por_pagina=None):
    letras = alfabeto
    livros_coletados = []
    
    for letra in letras:
        pagina_url = f"https://www.gutenberg.org/browse/titles/{letra}?sort_order=release_date"
        print(f"Acessando: {pagina_url}")

        # Passo 1: Contar o número total de livros únicos para a letra
        conteudo_html = acessar_pagina(pagina_url)
        if conteudo_html:
            soup = BeautifulSoup(conteudo_html, 'html.parser')
            livros = extrair_livros_da_pagina(pagina_url)
            ids_livros = set()
            for livro in livros:
                livro_id = livro['URL'].split('/')[-1]
                ids_livros.add(livro_id)
            total_livros_unicos = len(ids_livros)
        else:
            total_livros_unicos = 0

        # Passo 2: Coletar os detalhes dos livros únicos
        ids_livros = set()
        pagina_url = f"https://www.gutenberg.org/browse/titles/{letra}?sort_order=release_date"
        print(f"Acessando: {pagina_url}")
        livros = extrair_livros_da_pagina(pagina_url)
        for j, livro in enumerate(livros):
            if livros_por_pagina is not None and j >= livros_por_pagina:
                break

            livro_id = livro['URL'].split('/')[-1]
            if livro_id in ids_livros:
                continue  # Ignorar livros já coletados
            
            ids_livros.add(livro_id)  # Adicionar o ID ao conjunto

            detalhes_livro = obter_detalhes_do_livro(livro['URL'])
            if detalhes_livro:
                detalhes_livro['Title'] = livro['Title']
                detalhes_livro['URL'] = livro['URL']
                livros_coletados.append(detalhes_livro)
            print(f'Coleta realizada para livro {j+1} de {total_livros_unicos} livros únicos para a letra {letra} (alguns livros são repetidos, então ocorrem mais coletas do que o número total de livros)')
        
        print(f"{total_livros_unicos} livros únicos encontrados para a letra {letra}")

    salvar_livros_em_csv(livros_coletados)

# Executa o script de coleta de livros
if __name__ == '__main__':
    coletar_livros_de_gutenberg() # (alfabeto='abc', livros_por_pagina=3)

 
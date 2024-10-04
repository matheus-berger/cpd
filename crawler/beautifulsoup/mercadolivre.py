
# Importando a função de requisição do framework
import requests
# Importando as funções BeutifulSoup
from bs4 import BeautifulSoup
# imporando a biblioteca time
import time
# imporrando biblioteca choice
from random import choice
# importando bibliteca randint
from random import randint



# Lista de User-Agents
user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1'
]

# testando
def get_proxies_from_geonode(limit=500):
    """
    Extrai proxies da API Geonode e retorna uma lista de dicionários.

    Args:
        limit (int): Número máximo de proxies a serem retornados.

    Returns:
        list: Lista de dicionários, cada um representando um proxy.
    """

    url = "https://proxylist.geonode.com/api/proxy-list?protocols=https%2Chttp&limit={}&page=1&sort_by=lastChecked&sort_type=desc".format(limit)
    response = requests.get(url)
    data = response.json()

    proxies = []
    for proxy in data['data']:
        proxies.append({'ip': proxy['ip'], 'port': proxy['port']})

    return proxies


# Lista de Proxies
proxies_list = get_proxies_from_geonode()


# Função para obter um proxy aleatório da lista
def get_proxy():
    proxy = choice(proxies_list)
    return f"http://{proxy['ip']}:{proxy['port']}"

# Função para obter um User-Agent aleatório da lista
def get_user_agent():
    return choice(user_agents_list)


# Função para ler as paginas de categoria
def leitorPaginaCategoria(url, contador_paginas):


    # Cabeçalho customizado para utilizar na requisição, para o sistema do site da amazon reconhecer a requisisção como vindo de um navegador
    custom_headers = {
        "User-Agent": get_user_agent(),
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,pt-BR;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",  # Do Not Track request header
        "Upgrade-Insecure-Requests": "1"
    }
    

    # Variável que armazena a resposta da requisição
    response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy(), "http": get_proxy(), "http": get_proxy()})
    
    while response.status_code != 200 :
        segundos = randint(1, 3)
        print("print_status_pagina: ", response.status_code)
        time.sleep(segundos)
        response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy()})


    # Printando o resultado da requisição bem sucedida
    if contador_paginas > 1:
        print(f"{contador_paginas}ª pagina acessada com sucesso: {response.status_code}")
    else:
        print(f"Pagina inicial acessada com sucesso: {response.status_code}")

    # Criando o objeto soup para consultar informações dentro da pagina
    soup = BeautifulSoup(response.text, 'lxml')

    # Variavel para armazenar os links de produtos da pagina categoria
    link_elementos = soup.select("[data-asin] h2 a")


    # Acessa cada link de produto na pagina
    dados_produtos = []
    for link in link_elementos:
        link_completo = str('https://www.amazon.com.br' + link.attrs.get("href"))
        info_produto = leitorPaginaProduto(link_completo)
        print("> ", info_produto)
        dados_produtos.append(info_produto)
    
    

 

# Função para ler a pagina de um produto
def leitorPaginaProduto(url):
    
    # Cabeçalho customizado para utilizar na requisição, para o sistema do site da amazon reconhecer a requisisção como vindo de um navegador
    custom_headers = {
        "User-Agent": get_user_agent(),
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,pt-BR;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",  # Do Not Track request header
        "Upgrade-Insecure-Requests": "1"
    }
    

    # Variável que armazena a resposta da requisição
    response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy()})
    
    while response.status_code != 200 :
        segundos = randint(1, 3)
        print("print_status_produto: ", response.status_code)
        time.sleep(segundos)
        response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy()})


    try:

        # Criando o objeto soup para consultar informações dentro da pagina
        soup = BeautifulSoup(response.text, 'lxml')


        # Pegando o titulo do produto
        title_element = soup.select_one('#productTitle')
        titulo = title_element.text.strip() if title_element else None


        # Pegando a nota do produto
        avaliacao_elemento = soup.select_one('#acrPopover')
        avaliacao_texto = avaliacao_elemento.attrs.get('title') if avaliacao_elemento else None # Pegando a informação do atributo 'title'
        avaliacao = avaliacao_texto.replace(' de 5 estrelas', '') if avaliacao_texto else None # usando o método replace para armazenar somento o número

        # Pegando a quantidade de avaliações
        quantidadeAvaliacoes_elemento = soup.select_one('#acrCustomerReviewText')
        quantidadeAvaliacoes_text = quantidadeAvaliacoes_elemento.text.strip() if quantidadeAvaliacoes_elemento else None
        quantidadeAvaliacoes = quantidadeAvaliacoes_text.replace(' avaliações de clientes', '') if quantidadeAvaliacoes_text else None

        # Pegando o preço
        preco_elemento = soup.select_one('span.a-price.a-text-normal.aok-align-center.reinventPriceAccordionT2').select_one('span.a-offscreen')
        preco = preco_elemento.text if preco_elemento else None

        # Pegando a imagem
        imagem_elemento = soup.select_one('#landingImage')
            #print(imagem_elemento)
        imagem = imagem_elemento.attrs.get('scr')

        return {
            'titulo': titulo,
            'avaliacao': avaliacao,
            'quantidadeAvaliacoes': quantidadeAvaliacoes,
            'preco': preco,
            'imagem': imagem
        }

    except Exception as e:
        print(e)

# Função principal
def main():

    # Nome do arquivo CSV de saída
    arquivo_csv = 'dados.csv'

    url_inicial = "https://www.amazon.com.br/s?bbn=16194414011&rh=n%3A16194414011%2Cp_n_condition-type%3A13862762011&dc&qid=1728018162&rnid=13862761011&ref=lp_16194415011_nr_p_n_condition-type_0"

    quantidade_paginas = 1

    while quantidade_paginas != 10:
        data = leitorPaginaCategoria(url_inicial, quantidade_paginas)
        print(data)
 
        with open(arquivo_csv, 'w', newline='') as csvfile:
            
            
            fieldnames = None
            while fieldnames is None:
                for i in data:
                    if i is not None:
                        fieldnames = i.keys()  # Obtém os cabeçalhos das colunas dos dicionários
            
            # Criar um objeto escritor CSV
            writer = arquivo_csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Escrever o cabeçalho
            writer.writeheader()

            # Escrever as linhas de dados
            for row in data:
                writer.writerow(row) if row else 'N/a'
        

    
# Chamando a função principal
main()
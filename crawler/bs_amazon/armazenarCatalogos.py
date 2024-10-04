
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
# csv
import csv



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
        "Upgrade-Insecure-Requests": "1"
    }
    

    # Variável que armazena a resposta da requisição
    response = requests.get(url, headers=custom_headers)
    
    while response.status_code != 200 :
        segundos = randint(1, 3)
        print("print_status_pagina: ", response.status_code)
        time.sleep(segundos)
        response = requests.get(url, headers=custom_headers)


    # Printando o resultado da requisição bem sucedida
    if contador_paginas > 1:
        print(f"{contador_paginas}ª pagina acessada com sucesso: {response.status_code}")
    else:
        print(f"Pagina inicial acessada com sucesso: {response.status_code}")


    # Criando o objeto soup para consultar informações dentro da pagina
    soup = BeautifulSoup(response.text, 'lxml')

    # Adicionando a url da pagina atual no aquivo csv
    arquivo_csv = open('catalogos.csv', 'w')
    escritor = csv.writer(arquivo_csv)
    escritor.writerow([url])
    arquivo_csv.close()

    # Variavel para a proxima pagina
    proxima_pagina = soup.search.select_one('a:contains("Próximo")')
    if proxima_pagina:
        _url = proxima_pagina.attrs.get('href')
        proxima_url = str("https://www.amazon.com.br" + _url)

    # Armazena 10 links de paginas de categoria
    while contador_paginas <= 10:
        contador = contador_paginas + 1
        leitorPaginaCategoria(proxima_url, contador)


    
# Função principal
def main():


    url_inicial = 'https://www.amazon.com.br/s?bbn=16194414011&rh=n%3A16194414011%2Cp_n_condition-type%3A13862762011&dc&qid=1728035420&rnid=13862761011&ref=lp_16194415011_nr_p_n_condition-type_0'
                   
    quantidade_paginas = 1

    leitorPaginaCategoria(url_inicial, quantidade_paginas)

    
    
# Chamando a função principal
main()






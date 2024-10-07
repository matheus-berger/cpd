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
# re
import re



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


def leitorDadosProdutos(url, num_produto):
    
    # Cabeçalho customizado para utilizar na requisição, para o sistema do site da amazon reconhecer a requisisção como vindo de um navegador
    custom_headers = {
        "User-Agent": get_user_agent(),
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,pt-BR;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    # Variável que armazena a resposta da requisição
    response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy(), "http": get_proxy(), "http": get_proxy()})
    
    while response.status_code != 200 :
        response = requests.get(url, headers=custom_headers, proxies={"http": get_proxy(), "http": get_proxy(), "http": get_proxy()})

    
    try:

        # Criando o objeto soup para consultar informações dentro da pagina
        soup = BeautifulSoup(response.text, 'lxml')

        # Criando o objeto soup para consultar informações dentro da pagina
        soup = BeautifulSoup(response.text, 'lxml')

        # Pegando o título do produto
        title_element = soup.select_one('#productTitle')
        titulo = title_element.text.strip() if title_element else None

        # Pegando a nota do produto
        avaliacao_elemento = soup.select_one('#acrPopover')
        avaliacao_texto = avaliacao_elemento.attrs.get('title') if avaliacao_elemento else None
        avaliacao_valor = avaliacao_texto.replace(' de 5 estrelas', '') if avaliacao_texto else None
        avaliacao = float(avaliacao_valor.replace(',', '.'))


        # Pegando a quantidade de avaliações
        quantidadeAvaliacoes_elemento = soup.select_one('#acrCustomerReviewText')
        quantidadeAvaliacoes_text = quantidadeAvaliacoes_elemento.text.strip() if quantidadeAvaliacoes_elemento else None
        quantidadeAvaliacoes_valor = quantidadeAvaliacoes_text.replace(' avaliações de clientes', '') if quantidadeAvaliacoes_text else None
        quantidadeAvaliacoes = float(quantidadeAvaliacoes_valor)

        # Pegando o preço
        preco_whole_elemento = soup.select_one('div.a-section.a-spacing-none span.a-price-whole')
        #preco_whole_elemento2 = soup.select_one("#corePriceDisplay_desktop_feature_div .a-price-whole")
        preco_whole = preco_whole_elemento.text.strip().replace(',', '.')
        preco_fraction_elemento = soup.select_one("#corePriceDisplay_desktop_feature_div .a-price-fraction")
        preco_fraction = preco_fraction_elemento.text.strip()
        preco_text = preco_whole + preco_fraction
        preco = float(preco_text)

        
        # Pegando a quantidade de vendas no mês
        #vendasMes_elemento = soup.find('span', id='social-proofing-faceout-title-tk_bought').find('span', class_='a-text-bold selectorgadget_selected')
        vendasMes_elemento = soup.find('span', id='social-proofing-faceout-title-tk_bought').find('span')
        vendasMes_text = vendasMes_elemento.text
        inteiros = re.findall(r'\d+', vendasMes_text)
        inteiros = list(map(int, inteiros))
        vendasMes = inteiros[0]
        if 'mil' in vendasMes_text:
            vendasMes = vendasMes * 1000
        
        # Custo beneficio
        custoBeneficio = None
        if preco and avaliacao not in (None, ' ', ''):
            custoBeneficio = preco / avaliacao

        # Popularidade ajustada
        popularidadeAjustada = None
        if quantidadeAvaliacoes and avaliacao not in (None, ' ', ''):
            popularidadeAjustada = (quantidadeAvaliacoes * avaliacao) / 5 

        # Retornando lista com os dados
        return [titulo, avaliacao, quantidadeAvaliacoes, preco, vendasMes, custoBeneficio, popularidadeAjustada]

    except Exception as e:
        pass
        
            
# Função principal
def main():

    contador = 0

    # abrindo o arquivo dos catalogos e acessando seus links
    with open('produtos.csv', 'r') as arquivo:
      leitor = csv.reader(arquivo)
      
      # Acessando cada linha do arquivo
      for linha in leitor:
        link = str(linha[0]).strip()
        contador = contador + 1
        dados = leitorDadosProdutos(link, contador)
          
        # Escrevendo os dados se não for nulo  
        tentativas = 1
        while dados is None and tentativas <= 100:
            time.sleep(randint(1, 3))
            dados = leitorDadosProdutos(link, contador)
            tentativas = tentativas + 1
        if tentativas == 101:
            print(f"[ :( ] Não foi possivel acessar os dados do {contador}º produto! (Status do Prodututo: {dados})")
        else:
            # Vendo se os dados que foram armazenados de forma correta
            if dados[0] and dados[5] and dados[6] not in (None, ' ', ''):
                # Abrindo e escrevendo os dados no arquivo de dados
                with open('../memoriaExterna/dados.csv', 'a', newline='') as arquivoDados:
                    escritor = csv.writer(arquivoDados)
                    escritor.writerow(dados)
                    print(f"[ :D ] Dados do {contador}º produto salvos com sucesso!\n")
            else:
                print(f"[ :( ] Não foi possivel salvar os dados do {contador}º produto! (Dados Incompletos)") 

# Chamando a função principal
main()
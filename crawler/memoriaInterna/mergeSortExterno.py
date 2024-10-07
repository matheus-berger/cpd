import csv
import math
import os

def mergeSort(arquivoCSV, numeroLinhas, coluna):

    # Declarando a quantidade de linhas armazenada por cada chunck
    quantidadeLinhasChunck = math.ceil((numeroLinhas / 5))
    
    # Descobrindo a quantidade de chunks
    contadorChunks = 1

    # Linha percorrida
    linha = 0

    # Abrindo o arquivo CSV que será ordenado
    with open(arquivoCSV, 'r') as arquivo:
        reader = csv.reader(arquivo)
        
        # Chunck de memoria
        chunk = []

        # Percorre cada linha no arquivo da memoria externa
        for row in reader:
            # Adiciona a linha no chunk
            chunk.append(row)
            linha += 1
            
            # Quando atingir o limite de tamanho do chunk
            if linha >= quantidadeLinhasChunck:
                # Ordena o chunk
                tempExterno = sort(chunk, coluna)
                # Salva no arquivo temporario na memoria externa
                localTempExterno = f"C:\\Users\\User\\Documentos\\crawler_v2\\memoriaExterna\\temp{contadorChunks}.csv"
                with open(localTempExterno, 'a', newline='') as tempArquivoExterno:
                    writer = csv.writer(tempArquivoExterno)
                    writer.writerows(tempExterno)

                # Reset do chunk
                contadorChunks += 1
                chunk = []
                linha = 0

        # Se houverem linhas restantes no último chunk
        if chunk:
            # Ordena o último chunk
            tempExterno = sort(chunk, coluna)
            # Salva o último chunk
            localTempExterno = f"C:\\Users\\User\\Documentos\\crawler_v2\\memoriaExterna\\temp{contadorChunks}.csv"
            with open(localTempExterno, 'a', newline='') as tempArquivoExterno:
                writer = csv.writer(tempArquivoExterno)
                writer.writerows(tempExterno)


# Função Interna Ordenar
def sort(data, coluna):
     
    if len(data) <= 1:
        return data  # Caso base: lista com 1 ou menos elementos já está ordenada

    meio = len(data) // 2
    metadeEsquerda = data[:meio]
    metadeDireita = data[meio:]

    # Chama recursivamente para ordenar as metades
    metadeEsquerda = sort(metadeEsquerda, coluna)
    metadeDireita = sort(metadeDireita, coluna)

    # Mescla as duas metades ordenadas
    return merge(metadeEsquerda, metadeDireita, coluna)


# Função Interna Mesclar
def merge(esquerda, direita, coluna):
    
    result = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        vEsquerda = float(esquerda[i][coluna])
        vDireita = float(direita[j][coluna])
        if vEsquerda >= vDireita:
            result.append(esquerda[i])
            i += 1
        else:
            result.append(direita[j])
            j += 1  


    # Adiciona os elementos restantes (se houver)
    result.extend(esquerda[i:])
    result.extend(direita[j:])

    return result


def mergeExterno(diretorio, quantidade_arquivos, coluna, quantidade_produtos):
    
    # Caminho completo para o arquivo final (dados.csv)
    caminho_dados = os.path.join(diretorio, "dados.csv")
    
    # Lista para armazenar dados dos arquivos temporários
    dados_temporarios = []
    
    # Ler todos os arquivos temporários
    for i in range(1, quantidade_arquivos + 1):
        caminho_temp = os.path.join(diretorio, f"temp{i}.csv")
        dados_temporarios.append([])
        with open(caminho_temp, mode='r', newline='') as temp_file:
            leitor_csv = csv.reader(temp_file)
            for linha in leitor_csv:
                # Adicionar linha lida à lista de dados temporários
                dados_temporarios[i-1].append(linha)
    
    # pegando o index da coluna
    coluna = coluna-1

    # Salvando a maior linha
    maior = {
        'valor': 0,
        'temp': 0,
        'produto': 0
    }

    # Escrever os maiors dados de volta ao arquivo dados.csv
    with open(caminho_dados, mode='w', newline='') as arquivo_final:
        writer = csv.writer(arquivo_final)
        for linha_index in range(0, quantidade_produtos):
            for temp_index in range(0, len(dados_temporarios)):
                for produto_index in range(0, len(dados_temporarios[temp_index])):
                    valor = float(dados_temporarios[temp_index][produto_index][coluna])
                    if valor >= maior['valor']:
                        maior['valor'] = valor
                        maior['temp'] = temp_index
                        maior['produto'] = produto_index
                    produto_index = produto_index + 1
                temp_index = temp_index + 1
            #print(dados_temporarios[maior['temp']][maior['produto']])
            writer.writerow(dados_temporarios[maior['temp']][maior['produto']])
            del dados_temporarios[maior['temp']][maior['produto']] 
            if len(dados_temporarios[maior['temp']]) == 0:
                del dados_temporarios[maior['temp']]
            maior['valor'] = 0
            maior['temp'] = 0
            maior['produto'] = 0
        linha_index = linha_index + 1
    
    # deletando os arquivos temporarios
    for i in range(1, quantidade_arquivos+1):
        os.remove(os.path.join(diretorio, f"temp{i}.csv"))
        

def main():

    mergeSort(r"c:\\Users\\User\\Documentos\\crawler_v2\\memoriaExterna\\dados.csv", 47, 5)
    mergeExterno("c:\\Users\\User\\Documentos\\crawler_v2\\memoriaExterna\\", 5, 4, 47)

# Chamando Função main
main()
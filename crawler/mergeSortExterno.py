import os
import csv

# Diretórios
memoria_externa = 'memoria_externa'
memoria_interna = 'memoria_interna'
input_file = os.path.join(memoria_externa, 'produtos.csv')
output_file = os.path.join(memoria_externa, 'produtos_sorted.csv')

# Função para ler o arquivo CSV e dividir em chunks
def split_file(input_file, chunk_size=5):
    chunks = []
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                chunks.append(chunk)
                chunk = []
        if chunk:
            chunks.append(chunk)
    return header, chunks

# Função para ordenar cada chunk
def sort_chunk(chunk, key_index):
    return sorted(chunk, key=lambda x: float(x[key_index]))

# Função para mesclar dois chunks ordenados
def merge_chunks(chunk1, chunk2, key_index):
    merged = []
    i = j = 0
    while i < len(chunk1) and j < len(chunk2):
        if float(chunk1[i][key_index]) <= float(chunk2[j][key_index]):
            merged.append(chunk1[i])
            i += 1
        else:
            merged.append(chunk2[j])
            j += 1
    merged.extend(chunk1[i:])
    merged.extend(chunk2[j:])
    return merged

# Função para executar o Merge Sort Externo
def external_merge_sort(input_file, output_file, key_index, chunk_size=5):
    header, chunks = split_file(input_file, chunk_size)
    sorted_chunks = [sort_chunk(chunk, key_index) for chunk in chunks]
    
    while len(sorted_chunks) > 1:
        merged_chunks = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged_chunk = merge_chunks(sorted_chunks[i], sorted_chunks[i+1], key_index)
            else:
                merged_chunk = sorted_chunks[i]
            merged_chunks.append(merged_chunk)
        sorted_chunks = merged_chunks
    
    sorted_data = sorted_chunks[0]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(sorted_data)

# Índice da coluna "Vendas/Mês"
key_index = 4

# Executando o Merge Sort Externo
external_merge_sort(input_file, output_file, key_index)


''' Criando a tabela hash '''
M = 10 # Numero de Chaves da Tabela Hash

tabela_hash = list()
# Cria a Tabela Hash com 80 espaços para chaves
for x in range(0, M):
    tabela_hash.append(None)

# Criando uma lista de chaves
chaves = ["Chaves", "Kiko", "Nhonho", "Chiquinha", "Seu Madruga"]

# Função hash
def string_hash(s, M):
    h = 0
    for char in s:
        h = (31 * h + ord(char)) % M
        return h

print(tabela_hash)

# Inserindo valores a tabela_hash
def insert(s, indice):

print(tabela_hash)

# Armazenando as chaves na tabela_hash
for s in chaves:
    indice = string_hash(s, M)
    insert(s, indice)
    
    
    


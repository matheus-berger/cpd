
import math

# Função para pesquisa linear
def linearPesquisa(lista, valor):

    for i in range(len(lista)):
        if lista[i] == valor:
            return lista[i]
    return False

# Função para pesquisa em salto
def saltoPesquisa(lista, valor):
    
    inicio = lista[0]
    salto = int(math.sqrt(valor))

    if salto > len(lista):
        sub_lista = lista[0:]
        linearPesquisa(sub_lista, valor)
    else:
        sub_lista = lista[0:salto]
        encontrar = linearPesquisa(lista, valor)
        if encontrar != True:
            print(f"Valor {encontrar}, encontrado!")
        else:
            saltoPesquisa(sub_lista, valor)
        
# Funcao main
def main():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    saltoPesquisa(lista, 7)


# Chamando a funcao main
main()
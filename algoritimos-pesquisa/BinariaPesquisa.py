
import math

# Função para pesquisa binaria
def pesquisaBinaria(lista, valor):
   
    indice_inicio = 0
    indice_fim = len(lista)-1
    indice_meio = math.ceil((indice_inicio + indice_fim) / 2)
    
    
    if lista[indice_meio] == valor:
        print(f"Valor {lista[indice_meio]}, encontrado na posição {indice_meio}!")
        return 
    else: 
        if lista[indice_meio] < valor:
            sub_lista = lista[indice_meio:indice_fim]
            pesquisaBinaria(sub_lista, valor)
        else:
            sub_lista = lista[indice_inicio:indice_meio]
            pesquisaBinaria(sub_lista, valor)


# Função main
def main():
    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pesquisaBinaria(lista, 7)

    return True


# Chamando a função main
main()
"""
    02.1 - Implementar um algoritmo que implemente o Selection Sort.
        a. Testar com elementos já ordenados
        b. Testar com elementos ordenados na ordem inversa
        c. Testar com elementos duplicados
        d. Testar com elementos aleatórios sem repetição
"""

# Craindo a função selection_sort
def selection_sort(lista):
    
    # Percorre cada indice da lista
    for i in range(0, len(lista)):
        
        # Procura o menor numero no intervalo entre lista[i] e lista[len(lista) - 1]
        indiceMenor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[indiceMenor]:
                indiceMenor = j
        
        # Troca o menor numero com o numero de lista[i]
        aux = lista[i]
        lista[i] = lista[indiceMenor]
        lista[indiceMenor] = aux

    # Retorna a lista ordenada ao usuario
    return lista


# Craindo função main
def Main():
    
    print("\n:::::::::::::: ORDENANDO LISTAS (com Selection Sort) ::::::::::::::")

    # Testando com elementos já ordenados
    print("\n> [1º] Lista já ordenada: ")
    lista1 = [1, 2, 3, 4, 5, 6, 7]
    print("- Antes: ", lista1)
    lista1 = selection_sort(lista1)
    print("- Depois: ", lista1)

    # Testando com elementos ordenados na ordem inversa
    print("\n> [2º] Lista já ordenada inversa: ")
    lista2 = [7, 6, 5, 4, 3, 2, 1]
    print("- Antes: ", lista2)
    lista2 = selection_sort(lista2)
    print("- Depois: ", lista2)

    # Testando com elementos duplicados
    print("\n> [3º] Lista com elementos duplicados: ")
    lista3 = [7, 7, 1, 3, 3, 5, 1, 2, 5, 4, 6]
    print("- Antes: ", lista3)
    lista3 = selection_sort(lista3)
    print("- Depois: ", lista3)

    # Testando com elementos aleatórios sem repetição
    print("\n> [4º] Lista com elementos aleatórios sem repetição: ")
    lista4 = [77, 45, 33, 21, 10, 55, 76]
    print("- Antes: ", lista4)
    lista4 = selection_sort(lista4)
    print("- Depois: ", lista4)

    print("\n")


# Chamando função main
Main()

"""
    I. Tabelas de endereçamento direto são como armários organizados com várias gavetas; 
        Onde cada gaveta tem um número fixo (um "endereço"); 
        E você sabe exatamente em qual gaveta colocar ou buscar algo.

    II. Imagine que você tem uma lista de objetos, como livros; 
        Cada livro tem um número de identificação único, como 123, 456, 789, etc; 
        Agora, você quer guardar esses livros em um armário onde cada gaveta tem um número correspondente ao número do livro.
"""

# 01. Universo 'U' de chaves: O armario com as gavetas.
U = list()  

# 02. O armário precisa ter uma gaveta para cada número possível. 
#     Se os números dos livros forem de 1 a 1000, você precisa de um armário com 1000 gavetas.
quantidade_chaves = 1000
for i in range(0, (quantidade_chaves + 1)):
    U.append(i)

# 03. Tabela de endereços diretos 'T': A lista de Livros
T = list()

# 04. Cada posição, ou lacuna, corresponde a uma chave no universo U. 
#     Se o conjunto não contém nenhum elemento com chave k, então T[k] = NIL.

T = [None] * (quantidade_chaves + 1)


# 05. Funções [Inserir, Pesquisar, Deletar]
def search(T, k):
    # T = Tabela de Endereços diretos
    # k = A chave

    return T[k]


def insert(T, x):
    
    if x >= 1 and x <= 1000:
        if search(T, x) == None:
            T[x] = x
            return 1
        else:
            return "Chave já cadastrada!"
    else:
        return "Chave fora do Intervalo!"


def delete(T, x):

    if x >= 1 and x <= 1000:
        if search(T, x) == None:
            return "Já não existe cadastro com esta chave!"
        else:
            T[x] = None
            return 1
    else:
        return "Chave fora do Intervalo!"


# Função Main
def main():

    opc = 0
    while opc != 4:
        print("[ 1 ] Pesquisar Livro")
        print("[ 2 ] Adicionar Livro")
        print("[ 3 ] Remover Livro")
        print("[ 4 ] Sair")
        opc = int(input("> "))

        if opc == 1:
            k = int(input("Digite o codigo do livro: "))
            funcao = search(T, k)
            if funcao == None:
                print("Livro não cadastrado!")
            else:
                print(funcao)
        elif opc == 2:
            k = int(input("Digite o codigo do livro: "))
            funcao = insert(T, k)
            if funcao == 1:
                print("Livro cadastrado com sucesso!")
            else:
                print(funcao)
        elif opc == 3:
            k = int(input("Digite o codigo do livro: "))
            funcao = delete(T, k)
            if funcao == 1:
                print("Livro removido com sucesso!")
            else:
                print(funcao)
        elif opc == 4:
            print("Até Logo!")
        else:
            print("Opção invalida, tente novamente!")


# Chamando a função main
main()
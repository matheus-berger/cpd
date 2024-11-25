# Tabela de Endereços Diretos
quantidade_chaves = 1000
T = [None] * (quantidade_chaves + 1)  # Tabela com posições de 0 a 1000


def is_valid_key(k):
    """Valida se a chave está no intervalo permitido."""
    return 1 <= k <= quantidade_chaves


def search(T, k):
    """Busca por um elemento na tabela."""
    return T[k] if is_valid_key(k) else "Chave fora do intervalo!"


def insert(T, x):
    """Insere um elemento na tabela."""
    if not is_valid_key(x):
        return "Chave fora do intervalo!"
    if T[x] is None:
        T[x] = x
        return "Chave cadastrada com sucesso!"
    return "Chave já cadastrada!"


def delete(T, x):
    """Remove um elemento da tabela."""
    if not is_valid_key(x):
        return "Chave fora do intervalo!"
    if T[x] is not None:
        T[x] = None
        return "Chave removida com sucesso!"
    return "Chave não encontrada!"


def main():
    """Menu principal do programa."""
    while True:
        print("\n[ 1 ] Pesquisar Livro")
        print("[ 2 ] Adicionar Livro")
        print("[ 3 ] Remover Livro")
        print("[ 4 ] Sair")

        try:
            opc = int(input("> "))
        except ValueError:
            print("Entrada inválida, por favor insira um número.")
            continue

        if opc == 1:
            k = int(input("Digite o código do livro: "))
            print(search(T, k))
        elif opc == 2:
            k = int(input("Digite o código do livro: "))
            print(insert(T, k))
        elif opc == 3:
            k = int(input("Digite o código do livro: "))
            print(delete(T, k))
        elif opc == 4:
            print("Até logo!")
            break
        else:
            print("Opção inválida, tente novamente!")


# Chamando a função main
main()

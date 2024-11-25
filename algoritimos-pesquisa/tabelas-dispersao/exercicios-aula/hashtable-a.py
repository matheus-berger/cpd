"""
    01. Implemente uma hash table utilizando dicionários em Python:
        a. versão onde cada chave do dicińario refere-se a um vetor simples:
            htable = {key1: [], key2: []}
"""

# Classe node que representa cada chave
class Node:
    def __init__(self, dado, chave):
        self.dado = dado
        self.chave = chave 

# Classe para a tabela de endereços direto
class Table:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista_espaços = {} # Dicionario com os espaços para serem armazenados
        for i in range(0, tamanho):
            self.lista_espaços[i] = []
    

    def function_hash(self, dado):
        return dado % self.tamanho

    def inserir(self, dado):
        chave = self.function_hash(dado)
        node = Node(dado, chave)
        self.lista_espaços[node.chave].append(node)
    
    def pesquisar(self, dado):
        chave = self.function_hash(dado)
        conteteudo_indice = self.lista_espaços[chave]
        if len(conteteudo_indice) != 0:
            for node in conteteudo_indice:
                if node.dado == dado:
                    return node
            return None # Nenhum node com este dado encontrado
        else:
            return None # Indice vazio
    
    def remover(self, dado):
        chave = self.function_hash(dado)
        conteteudo_indice = self.lista_espaços[chave]
        if len(conteteudo_indice) != 0:
            for node in conteteudo_indice:
                if node.dado == dado:
                    conteteudo_indice.remove(node)
                    return 1
            return None # Nenhum node com este dado encontrado
        else:
            return None # Indice vazio


# Criando classe Main
class Main:
    def __init__(self):
        self.table = None
    
    # Criando função Main
    def main(self):
        
        # Criando Menu
        while True:
            print("\n>==== Tabela de Dispersao - Com Dicionarios ====<")
            print("[ 1 ] - Criar Tabela")
            print("[ 2 ] - Adicionar um Valor")
            print("[ 3 ] - Remover um Valor")
            print("[ 4 ] - Procurar um Valor")
            print("[ 5 ] - Sair")
            opc = int(input("> "))

            # Verificando a opção escolhida
            if opc == 1:  # Criação da Tabela
                print("\n[> ] Criação da Tabela:")
                if self.table is not None:
                    print("A tabela já está criada!")
                else:
                    tamanho_tabela = int(input("Digite o tamanho da tabela: "))
                    self.table = Table(tamanho_tabela)
                    print(f"Tabela de tamanho {self.table.tamanho} criada com sucesso!")
            elif opc == 2:  # Inserção de um valor
                print("\n[> ] Adicionar um valor:")
                if self.table is not None:
                    valor = int(input("Insira o valor: "))
                    self.table.inserir(valor)
                    print(f"Nó de chave e valor {valor} inserido na tabela com sucesso!")
                else:
                    print("Por favor, crie a Tabela antes de inserir um valor!")
            elif opc == 3:  # Remover um valor
                print("\n[> ] Remoção de um valor:")
                if self.table is not None:
                    valor = int(input("Insira o valor do nó que você quer remover: "))
                    remocao = self.table.remover(valor)
                    if remocao == 1:
                        print("Nó removido com sucesso!")
                    else:
                        print("Valor não encontrado!")
                else:
                    print("Por favor, crie a Tabela antes de querer remover um valor!")
            elif opc == 4:  # Buscar por Valor
                print("\n[> ] Busca de Valor:")
                if self.table is not None: 
                    valor = int(input("Digite o Valor: "))
                    encontrado = self.table.pesquisar(valor)
                    if encontrado == None:
                        print("Valor não encontrado!")
                    else:
                        print(f"Node de valor {encontrado.dado} encontrado!")
                else:
                    print("Por favor, crie a Tabela antes de pesquisar um valor!")
            elif opc == 5:  # Fechando o programa
                print("Tem certeza que deseja sair? Sua atividade não será salva!")
                opc_sair = input("[y / n]: ").upper()
                if opc_sair == "Y":
                    print("Desligando o Sistema...")
                    break
            else:
                print("Opção Inválida!")
    

# Ponto de entrada do programa
if __name__ == "__main__":
    app = Main()  # Instancia a classe Main
    app.main()    # Chama o método main()
      
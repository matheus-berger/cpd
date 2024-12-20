
# Classe node que representa cada chave
class Node:
    def __init__(self, dado):
        self.chave = dado
        self.dado = dado 

# Classe para a tabela de endereços direto
class Table:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista_espaços = [None] * (tamanho + 1) # Criando uma array de tamanho fixo

    def inserir_direto(self, node):
        self.lista_espaços[node.chave] = node
    
    def retornar_direto(self, chave):
        return self.lista_espaços[chave]
    
    def remover_direto(self, chave):
        self.lista_espaços[chave] = None


# Criando classe Main
class Main:
    def __init__(self):
        self.table = None
    
    # Criando função Main
    def main(self):
        
        # Criando Menu
        while True:
            print("\n>==== Tabela de Dispersao - Endereçamento Direto ====<")
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
                    if valor > self.table.tamanho:
                        print("Valor com chave maior que a tabela! Tente Novamente.")
                    else:
                        valor_repetido = self.table.retornar_direto(valor)
                        if valor_repetido != None: 
                            print("Um nó com chave de mesmo valor já foi inserido!")
                        else:
                            newnode = Node(valor)
                            self.table.inserir_direto(newnode)
                            print(f"Nó de chave e valor {newnode.chave} inserido na tabela com sucesso!")
                else:
                    print("Por favor, crie a Tabela antes de inserir um valor!")
            elif opc == 3:  # Remover um valor
                print("\n[> ] Remoção de um valor:")
                if self.table is not None:
                    chave = int(input("Insira a chave do nó que você quer remover: "))
                    if chave > self.table.tamanho:
                        print("A chave excede o tamanho da tabela! Tente novamente.")
                    else:
                        remover_node = self.table.retornar_direto(chave)
                        if remover_node is not None:
                            self.table.remover_direto(remover_node.chave)
                            print(f"Nó de chave e valor {chave} removido da Tabela com sucesso!")
                        else:
                            print(f"Nenhum nó de chave {chave} encontrado na Tabela!")
                else:
                    print("Por favor, crie a Tabela antes de querer remover um valor!")
            elif opc == 4:  # Buscar por Valor
                print("\n[> ] Busca de Valor:")
                if self.table is not None: 
                    chave = int(input("Digite a Valor: "))
                    if chave > self.table.tamanho:
                        print("Valor maior que o tamanho da lista, não há chave para ele! Tente Novamente.")
                    else:
                        node_encontrado = self.table.retornar_direto(chave)
                        if node_encontrado is None:
                            print(f"Nenhum nó de chave {chave} encontrado!")
                        else:
                            print(f"Nó de chave {node_encontrado.chave} encontrado!")
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
      
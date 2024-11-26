"""
    01. Implemente uma hash table utilizando dicionários em Python:
        b. versão com lista encadeadas.       
"""


# Classe node que representa cada chave
class Node:
    def __init__(self, dado, chave):
        self.dado = dado
        self.chave = chave 
        self.anterior = None
        self.posterior = None

# Classe para a tabela de endereços direto
class Table:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista_espaços = {}  # Dicionário para armazenar listas encadeadas
        for i in range(tamanho):
            self.lista_espaços[i] = None  # Inicializa como None para cada espaço
    
    def function_hash(self, dado):
        return dado % self.tamanho

    def inserir(self, dado):
        chave = self.function_hash(dado)
        novo_node = Node(dado, chave)

        # Verifica se há um nó já armazenado na posição
        if self.lista_espaços[chave] is None:
            # Nenhuma colisão, adiciona diretamente
            self.lista_espaços[chave] = novo_node
        else:
            # Colisão encontrada, percorre até o final da lista encadeada
            atual_node = self.lista_espaços[chave]
            while atual_node.posterior is not None:
                atual_node = atual_node.posterior
            # Adiciona o novo nó no final da lista
            atual_node.posterior = novo_node
            novo_node.anterior = atual_node
                
    
    def pesquisar(self, dado):
        chave = self.function_hash(dado)

        # Verifica se há um nó já armazenado na posição
        if self.lista_espaços[chave] is None:
            return None # Nada encontrado no indice
        else:
            # Procura o node com o dado informado no parametro da função
            atual_node = self.lista_espaços[chave]
            while atual_node is not None and atual_node.dado != dado:
                atual_node = atual_node.posterior
            # Retorna o que foi encontrado
            return atual_node # Se não foi encontrado == None
        
    
    def remover(self, dado):
        # Pega a chave do dado
        chave = self.function_hash(dado)

        # Procuca o node na tabela
        node_procurado = self.pesquisar(dado)

        if node_procurado == None:
            return node_procurado # retorna None
        else:
            if node_procurado.anterior is None: # É o primeiro da lista
                if node_procurado.posterior is None: # É o unico da lista
                    self.lista_espaços[chave] = None
                else: # Não é o unico da lista
                    self.lista_espaços[chave] = node_procurado.posterior
                    node_procurado.posterior = None
            else: # Não é o primeiro da lista
                if node_procurado.posterior is None: # É o ultimo da lista
                    node_procurado.anterior.posterior = None
                    node_procurado.anterior = None
                else: # Não é o ultimo da lista
                    node_procurado.anterior.posterior = node_procurado.posterior
                    node_procurado.posterior.anterior = node_procurado.anterior
            # Retornando resultado de exclusão bem sucedida
            return 1

# Criando classe Main
class Main:
    def __init__(self):
        self.table = None
    
    # Criando função Main
    def main(self):
        
        # Criando Menu
        while True:
            print("\n>==== Tabela de Dispersao - Com Lista Encadeada ====<")
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
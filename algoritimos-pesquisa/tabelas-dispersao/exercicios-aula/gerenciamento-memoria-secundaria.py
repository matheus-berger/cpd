
"""
    I.  Uma empresa de tecnologia está desenvolvendo um sistema de gerenciamento de arquivos
        armazenados em memória secundária (discos rígidos ou SSDs).
    II. A empresa quer implementar uma tabela hash para organizar os arquivos com base no nome
        do arquivo como chave.
"""

# Classe node que representa cada arquivo
class Node:
    def __init__(self, nome, caminho, tamanho, chave):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho
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
    

    # Função Hash para strings
    def function_hash(self, nome):
        h = 0
        for char in nome:
            h = (31 * h + ord(char)) % self.tamanho
        return h


    def inserir(self, nome, caminho, tamanho):
        chave = self.function_hash(nome)
        novo_node = Node(nome, caminho, tamanho, chave)

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
                
    
    def pesquisar(self, nome):
        chave = self.function_hash(nome)

        # Verifica se há um nó já armazenado na posição
        if self.lista_espaços[chave] is None:
            return None # Nada encontrado no indice
        else:
            # Procura o node com o nome informado no parametro da função
            atual_node = self.lista_espaços[chave]
            while atual_node is not None and atual_node.nome != nome:
                atual_node = atual_node.posterior
            # Retorna o que foi encontrado
            return atual_node # Se não foi encontrado == None
        
    
    def remover(self, nome):
        # Pega a chave do nome
        chave = self.function_hash(nome)

        # Procuca o node na tabela
        node_procurado = self.pesquisar(nome)

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
    

    # Função para listar todos os arquivos existentes
    def listar_arquivos(self):
        for chave in range(0, self.tamanho):
            if self.lista_espaços[chave] is not None:
                atual_node = self.lista_espaços[chave]
                while atual_node is not None:
                    print(f"ID: {atual_node.chave} | Nome: {atual_node.nome} | Caminho: {atual_node.caminho} | Tamanho: {atual_node.tamanho}")
                    atual_node = atual_node.posterior


# Criando classe Main
class Main:
    def __init__(self):
        self.table = None
    
    # Criando função Main
    def main(self):
        
        # Criando Menu
        while True:
            print("\n>==== Gerenciado de Memoria Secundaria ====<")
            print("[ 1 ] - Criar Tabela")
            print("[ 2 ] - Adicionar um Arquivo")
            print("[ 3 ] - Remover um Arquivo")
            print("[ 4 ] - Procurar um Arquivo")
            print("[ 5 ] - Listar Todos os Arquivos")
            print("[ 6 ] - Sair")
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
            elif opc == 2:  # Inserção de um arquivo
                print("\n[> ] Adicionar um Arquivo:")
                if self.table is not None:
                    nome = str(input("Insira o nome do arquivo: "))
                    caminho = str(input("Insira o caminho do arquivo: "))
                    tamanho = int(input("Insira o tamanho do arquivo (em KB): "))
                    self.table.inserir(nome, caminho, tamanho)
                    print(f"Arquivo de nome {nome} inserido na tabela com sucesso!")
                else:
                    print("Por favor, crie a Tabela antes de inserir um Arquivo!")
            elif opc == 3:  # Remover um arquivo
                print("\n[> ] Remoção de um arquivo:")
                if self.table is not None:
                    nome = str(input("Insira o nome do arquivo que você quer remover: "))
                    remocao = self.table.remover(nome)
                    if remocao == 1:
                        print("Arquivo removido com sucesso!")
                    else:
                        print("Arquivo não encontrado!")
                else:
                    print("Por favor, crie a Tabela antes de querer remover um arquivo!")
            elif opc == 4:  # Buscar por Arquivo
                print("\n[> ] Busca de Arquivo:")
                if self.table is not None: 
                    nome = str(input("Digite o nome do arquivo: "))
                    encontrado = self.table.pesquisar(nome)
                    if encontrado == None:
                        print("Arquivo não encontrado!")
                    else:
                        print(f"Arquivo de nome {encontrado.nome} encontrado!")
                else:
                    print("Por favor, crie a Tabela antes de buscar um arquivo!")
            elif opc == 5: # Listando todos os arquivos
                print("\n[> ] Listando todos os Arquivos:")
                if self.table is not None: 
                    self.table.listar_arquivos()
                else:
                    print("Por favor, crie a Tabela antes de listar os arquivos!")
            elif opc == 6:  # Fechando o programa
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
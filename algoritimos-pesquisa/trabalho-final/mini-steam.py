"""     

    Fontes auxiliares:
        1 - Algoritmos - Teoria e Prática: Thomas Cormen
        2 - Python Data Structures and Algorithms: Benjamin Baka
        3 - Correção e Resolução de Bugs: ChatGPT

"""

# Classe nó, que será um objeto.
class Jogo:
    def __init__(self, id, nome, desenvolvedor, preco, generos):
        self.id = id # Valor do ID do jogo
        self.nome = nome
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos
        self.p = None # Arvore: Objeto pai
        self.esquerda = None # Arvore: Objeto filho a esquerda
        self.direita = None # Arvore: Objeto filho a direita
        self.posterior = None # Tabela: Ponteiro objeto posterior
        self.anterior = None # Tabela: Ponteiro objeto anterior


# Hash tables de endereçamento direto para armazenar os IDs unicos
class IDs_table:
    def __init__(self, quantida_maxima_ids):
        self.quantidade_ids = quantida_maxima_ids
        self.lista_ids_ocupado = {}  # Dicionário que armazena os ids sendo usados
        for i in range(1, self.quantidade_ids + 1):
            self.lista_ids_ocupado[i] = None  # Inicializa como None para cada espaço
        self.lista_ids_livre = []
        for i in range(1, self.quantidade_ids + 1):
            self.lista_ids_livre.append(i) # Preenche a lista com o todas de ids livres
    
    # Função para usar um id
    def usar(self):
        if len(self.lista_ids_livre) > 0:
            id = self.lista_ids_livre[0] # Armazena o ID livre
            self.lista_ids_livre.pop(0) # Remove o ID livre da lista dos Livres
            self.lista_ids_ocupado[id] = id # Utiliza o id no dicionario de ocupados
            return True
        else:
            print("Não há mais IDs disponiveis!")
            return False

    # Função para liberar um id
    def liberar(self, id):
        if id > self.quantidade_ids:
            print("Este id não existe!")
            return False
        else:
            if self.lista_ids_ocupado[id] == None:
                print("Este ID já esta em uso!")
                return False
            else:
                self.lista_ids_ocupado[id] = None
                self.lista_ids_livre.append(id)
                return True


# Classe Arvore Binaria, estrutura de dados ligada, na qual cada nó é um objeto.
class BinaryTree:
    def __init__(self):
        self.raiz = None  # Inicialmente, a árvore está vazia

    # Função para inserir um novo valor na árvore
    def Tree_Insert(self, novonode):
        
        painode = None
        atualnode = self.raiz
        while atualnode != None:
            painode = atualnode
            if novonode.preco < atualnode.preco:
                atualnode = atualnode.esquerda
            else: 
                atualnode = atualnode.direita
        novonode.p = painode
        if painode == None:
            self.raiz = novonode   # A árvore é vazia
        elif novonode.preco < painode.preco:
            painode.esquerda = novonode
        else:
            painode.direita = novonode


    # Função para jogos por preco chave
    def buscar_preco(self, preco):
        def buscar_recursivo(node):
            if node is None:
                return []
            if node.preco == preco:
                return [node] + buscar_recursivo(node.esquerda) + buscar_recursivo(node.direita)
            elif preco < node.preco:
                return buscar_recursivo(node.esquerda)
            else:
                return buscar_recursivo(node.direita)
        return buscar_recursivo(self.raiz)


    # Função para jogos por margem de preco
    def buscar_faixa(self, preco_min, preco_max):
        def buscar_recursivo(node):
            if node is None:
                return []
            resultados = []
            if preco_min <= node.preco <= preco_max:
                resultados.append(node)
            if node.preco > preco_min:
                resultados += buscar_recursivo(node.esquerda)
            if node.preco < preco_max:
                resultados += buscar_recursivo(node.direita)
            return resultados
        return buscar_recursivo(self.raiz)


# Classe para a tabela de endereços direto
class Table:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista_espaços = {}  # Dicionário para armazenar listas encadeadas
        for i in range(tamanho):
            self.lista_espaços[i] = None  # Inicializa como None para cada espaço
    

    # Função Hash para strings
    def function_hash(self, genero):
        h = 0
        for char in genero:
            h = (31 * h + ord(char)) % self.tamanho
        return h
    
    # Função para inserir um jogo 
    def inserir(self, node):
        novo_node = node
        for genero in node.generos:
            chave = self.function_hash(genero)
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
                
    
    def pesquisar(self, genero):
        chave = self.function_hash(genero)

        # Verifica se há algo armazenado no indice da tabela
        if self.lista_espaços[chave] is None:
            return None # Nada encontrado no indice
        else:
            # Procura o node com o genero informado no parametro da função
            lista_encontrados = []
            atual_node = self.lista_espaços[chave]
            while atual_node is not None:
                if genero in atual_node.generos:
                    lista_encontrados.append(atual_node)
                atual_node = atual_node.posterior
            # Retorna o que foi encontrado
            if len(lista_encontrados) > 0:
                return lista_encontrados 
            else: # Se não foi encontrado == None
                return None


# Criando a classe Main
class Main:
    def __init__(self):
        self.abb = BinaryTree()
        self.listaIDs = IDs_table(30) # Conjunto de 30 ids para serem utilizados
        self.table = Table(30) # hash table para os generos
    
    # Método Main
    def main(self):
        # Menu de Opções:
        while True:
            print("\n>==== Gerenciamento mini-Steam ====<")
            print("[ 1 ] - Cadastrar Jogo")
            print("[ 2 ] - Pesquisa por Preço")
            print("[ 3 ] - Pesquisar Por Genero")
            print("[ 4 ] - Sair")
            opc = int(input("> "))

            # Verificando a opção escolhida
            if opc == 1:  # Cadastrar Produto
                print("\n[> ] Cadastrar um Jogo:")
                id = self.listaIDs.usar()
                if id:
                        # Armazenando o nome
                    nome = str(input("Digite o Nome do Jogo: "))
                        # Armazenando o desenvolvedor
                    desenvolvedor = str(input("Digite a Nome do Desenvolvedor do Jogo: "))
                        # Armazenando o preco
                    preco = float(input("Digite o Preco do Jogo R$: "))
                        # Armazenando os generos
                    generos = str(input("Digite os generos [Separados por ',']: "))
                        # Tira os espaços na frente e atraz de cada genero e os coloca em uma lista
                    lista_generos = [palavra.strip() for palavra in generos.split(',')]
                    jogo = Jogo(id, nome, desenvolvedor, preco, lista_generos)
                    # Inserindo o Jogo na arvore de precos
                    self.abb.Tree_Insert(jogo)
                    # Inserindo o Jogo na Tabela de Generos
                    self.table.inserir(jogo)
                    # Retorando o resultado para o usuario
                    print(f"Jogo cadastrado com sucesso!")
                else:
                    print("Não foi possivel adicionar um novo jogo, pois não há mais IDs disponiveis.")
            elif opc == 2:  # Buscar por preco
                print("\n[> ] Busca por Preco:")
                if self.abb.raiz is not None: 
                    print("[ 1 ] - Busca por Preco")
                    print("[ 2 ] - Busca por Média de Preco")
                    print("[ 3 ] - Sair")
                    opc_busca_preco = int(input("> "))
                    if opc_busca_preco == 1: # Busca por preco especifico
                        print("[> ] Busca por Preco:")
                        preco_pesquisar = float(input("Digite o Preco: "))
                        jogos_por_preco = self.abb.buscar_preco(preco_pesquisar)
                        print(f"Jogos que custam R${preco_pesquisar}:")
                        if len(jogos_por_preco) == 0:
                            print("Não há nenhum jogo por esse preco!")
                        else:
                            for jogo in jogos_por_preco:
                                print(f" Nome: {jogo.nome} | Preço: {jogo.preco}")
                    elif opc_busca_preco == 2: # Busca por media de preco
                        print("[> ] Busca por Faixa:")
                        preco_minimo = float(input("Digite o Preco Minimo: "))
                        preco_maximo = float(input("Digite o Preco Maximo: "))
                        jogos_por_faixa = self.abb.buscar_faixa(preco_minimo, preco_maximo)
                        print(f"Jogos que na faixa de preço entre R${preco_minimo} e R${preco_maximo}:")
                        if len(jogos_por_faixa) == 0:
                            print("Não há nenhum jogo nessa faixa de preco!")
                        else:
                            for jogo in jogos_por_faixa:
                                print(f" Nome: {jogo.nome} | Preço: {jogo.preco}")
                    elif opc_busca_preco == 3: # Saindo do menu de busca de preco
                        print("Saindo do menu...")
                    else:
                        print("Opção Invalida, tente novamente!")
                else:
                    print("Não há nenhum produto cadastrado, por favor cadastre um produto primeiramente.")
            elif opc == 3:  # Buscar por genero
                print("\n[> ] Busca por Genero: ")
                genero = str(input("Digite o Genero: "))
                encontrados = self.table.pesquisar(genero)
                if encontrados == None:
                    print("Nenhum jogo com este genero foi encontrado!")
                else:
                    print("Lista de Jogos do Genero {genero}:")
                    for jogo in encontrados:
                        print(f"Nome: {jogo.nome} | Preco: R${jogo.preco} | Genero: {jogo.generos}")
            elif opc == 4:  # Fechando o programa
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
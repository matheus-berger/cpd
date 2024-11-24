"""
    03. Uma empresa de e-commerce armazena informações sobre seus produtos e quer otimizar a
        busca por eles. Cada produto possui um código numérico único que representa seu ID, além de
        outras informações como nome, descrição e preço.
        > A empresa precisa de um sistema onde seja possível:
            I. Inserir um novo produto de forma eficiente.
            II. Remover um produto com base no seu ID.
            III. Buscar um produto rapidamente pelo seu ID.
            IV. Listar os produtos em ordem crescente de ID.
    
    Fontes auxiliares:
        1 - Algoritmos - Teoria e Prática: Thomas Cormen
        2 - Python Data Structures and Algorithms: Benjamin Baka
        3 - Correção e Resolução de Bugs: ChatGPT

"""

# Classe nó, que será um objeto.
class Node:
    def __init__(self, chave, nome, descricao, preco):
        self.chave = chave # Valor do ID do produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.p = None # Objeto pai
        self.esquerda = None # Objeto filho a esquerda
        self.direita = None # Objeto filho a direita


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
            if novonode.chave < atualnode.chave:
                atualnode = atualnode.esquerda
            else: 
                atualnode = atualnode.direita
        novonode.p = painode
        if painode == None:
            self.raiz = novonode   # A árvore é vazia
        elif novonode.chave < painode.chave:
            painode.esquerda = novonode
        else:
            painode.direita = novonode


    # Função para percorrer e printar os elementos da arvore (In-Order)
    def In_Order_Walk(self, x):
        if x is not None:
            self.In_Order_Walk(x.esquerda)
            print(f"ID: {x.chave} | Nome: {x.nome} | Descrição: {x.descricao} | Preco: R$ {x.preco}")
            self.In_Order_Walk(x.direita)


    # Função para pesquisar chave
    def Iterative_Tree_Search(self, atualnode, chave_search):

        while atualnode != None and chave_search != atualnode.chave:
            if chave_search < atualnode.chave:
                atualnode = atualnode.esquerda
            else:
                atualnode = atualnode.direita
        return atualnode


    # Função para enncontrar o node com valor minimo dentro da arvore ou sub-arvore
    def Tree_Minimum(self, node_raiz):
        while node_raiz.esquerda != None:
            node_raiz = node_raiz.esquerda
        return node_raiz


    # Subrotina para movimentar sub-árvores
    def Transplant(self, u, v):
        if u.p == None:
            self.raiz = v
        elif u == u.p.esquerda:
            u.p.esquerda = v
        else:
            u.p.direita = v 
        if v != None:
            v.p = u.p


    # Função para deletar um nó da árvore
    def Tree_Delete(self, node_remover):
        if node_remover.esquerda == None:
            self.Transplant(node_remover, node_remover.direita)
        elif node_remover.direita == None:
            self.Transplant(node_remover, node_remover.esquerda)
        else:
            y = self.Tree_Minimum(node_remover.direita)
            if y.p != node_remover:
                self.Transplant(y, y.direita)
                y.direita = node_remover.direita
                y.direita.p = y
            self.Transplant(node_remover, y)
            y.esquerda = node_remover.esquerda
            y.esquerda.p = y


# Criando a classe Main
class Main:
    def __init__(self):
        self.abb = BinaryTree()
    
    # Método Main
    def main(self):
        # Menu de Opções:
        while True:
            print("\n>==== ABB e-Shop ====<")
            print("[ 1 ] - Cadastrar Produto")
            print("[ 2 ] - Remover Produto")
            print("[ 3 ] - Buscar Produto")
            print("[ 4 ] - Listar Todos os Produtos")
            print("[ 5 ] - Sair")
            opc = int(input("> "))

            # Verificando a opção escolhida
            if opc == 1:  # Cadastrar Produto
                print("\n[> ] Cadastrar Produto:")
                chave = int(input("Insira o ID do produto [Insira 0 Para Voltar]: ")) # Receber ID
                if chave != 0:
                    if self.abb.raiz is not None:
                        procurar_node = self.abb.Iterative_Tree_Search(self.abb.raiz, chave) # Pesquisar e validar ID
                        while procurar_node is not None and chave != 0:
                            print("ID já cadastrado!")
                            chave = int(input("Insira outro ID para o produto [Insira 0 Para Voltar]: "))
                        if chave != 0: # Cadastra Produto
                            nome_produto = str(input("Digite o Nome do Produto: "))
                            descricao_produto = str(input("Digite a Descrição do Produto: "))
                            preco_produto = float(input("Digite o Preco do Produto R$: "))
                            produto = Node(chave, nome_produto, descricao_produto, preco_produto)
                            self.abb.Tree_Insert(produto)
                            print(f"Produto de ID {produto.chave} cadastrado com sucesso!")
                    else: # Cadastrar Produto
                        nome_produto = str(input("Digite o Nome do Produto: "))
                        descricao_produto = str(input("Digite a Descrição do Produto: "))
                        preco_produto = float(input("Digite o Preco do Produto R$: "))
                        produto = Node(chave, nome_produto, descricao_produto, preco_produto)
                        self.abb.Tree_Insert(produto)
                        print(f"Produto de ID {produto.chave} cadastrado com sucesso!")
            elif opc == 2:  # Remover Produto
                print("\n[> ] Remoção de Produto:")
                if self.abb.raiz is not None:
                    chave = int(input("Insira o ID do produto a ser removido: "))
                    remover_node = self.abb.Iterative_Tree_Search(self.abb.raiz, chave)
                    if remover_node is not None:
                        print("Deseja remover o produto: ")
                        print(f"ID: {remover_node.chave} | Nome: {remover_node.nome} | Descrição: {remover_node.descricao} \n| Preco: R$ {remover_node.preco}")
                        opc_remover = input("[y / n] > ").upper()
                        if opc_remover == 'Y':
                            self.abb.Tree_Delete(remover_node)
                            print(f"Produto removido com sucesso!")
                    else:
                        print(f"Nenhum produto de ID {chave} encontrado!")
                else:
                    print("Não há nenhum produto cadastrado, por favor cadastre um produto primeiramente.")
            elif opc == 3:  # Buscar Produto
                print("\n[> ] Busca de Chave:")
                if self.abb.raiz is not None: 
                    chave = int(input("Digite o ID do Produto: "))
                    node_encontrado = self.abb.Iterative_Tree_Search(self.abb.raiz, chave)
                    if node_encontrado is None:
                        print(f"Nenhum produto de ID {chave} encontrado!")
                    else:
                        print("Produto Encontado:")
                        print(f"ID: {node_encontrado.chave} | Nome: {node_encontrado.nome} | Descrição: {node_encontrado.descricao} | Preco: R$ {node_encontrado.preco}")
                else:
                    print("Não há nenhum produto cadastrado, por favor cadastre um produto primeiramente.")
            elif opc == 4:  # Listar Produtos
                print("\n[> ] Lista de Todos os Produtos (por ID):") 
                if self.abb.raiz is None:
                    print("Não há nenhum produto cadastrado, por favor cadastre um produto primeiramente.")
                else:
                    self.abb.In_Order_Walk(self.abb.raiz)
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
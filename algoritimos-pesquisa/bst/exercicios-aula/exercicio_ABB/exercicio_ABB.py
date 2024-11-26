"""
    01. Crie um TAD (Tipo Abstrato de Dados) de ABB, com, no mínimo, funções para:
        ○ criação;
        ○ inserção;
        ○ impressão (percurso em pré-ordem, pós-ordem, ordem simétrica);
        ○ deleção;
        ○ busca.
    
    Fontes auxiliares:
        1 - Algoritmos - Teoria e Prática: Thomas Cormen
        2 - Python Data Structures and Algorithms: Benjamin Baka
        3 - Correção e Resolução de Bugs: ChatGPT

"""

# Classe nó, que será um objeto.
class Node:
    def __init__(self, chave):
        self.chave = chave # Valor da Chave
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
            print(x.chave, end=' ')
            self.In_Order_Walk(x.direita)


    # Função para percorrer e printar os elementos da arvore (Pre-Order)
    def Pre_Order_Walk(self, x):
        if x is not None:
            print(x.chave, end=' ')  # Visita o nó atual
            self.Pre_Order_Walk(x.esquerda)  # Subárvore esquerda
            self.Pre_Order_Walk(x.direita)  # Subárvore direita


    # Função para percorrer e printar os elementos da arvore (Post-Order)
    def Post_Order_Walk(self, x):
        if x is not None:
            self.Post_Order_Walk(x.esquerda)  # Subárvore esquerda
            self.Post_Order_Walk(x.direita)  # Subárvore direita
            print(x.chave, end=' ')  # Visita o nó atual


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
        self.abb = None
    
    # Método Main
    def main(self):
        # Menu de Opções:
        while True:
            print("\n>==== Menu Árvore ABB ====<")
            print("[ 1 ] - Criar Árvore ABB")
            print("[ 2 ] - Inserir Chave")
            print("[ 3 ] - Deletar Chave")
            print("[ 4 ] - Imprimir a Árvore")
            print("[ 5 ] - Pesquisar Chave")
            print("[ 6 ] - Sair")
            opc = int(input("> "))

            # Verificando a opção escolhida
            if opc == 1:  # Criação da Árvore
                print("\n[> ] Criação de Árvore ABB:")
                if self.abb is not None:
                    print("A árvore já está criada!")
                else:
                    self.abb = BinaryTree()
                    print("Árvore ABB criada com sucesso!")
            elif opc == 2:  # Inserção de Chave
                print("\n[> ] Inserção de Chave:")
                if self.abb is not None:
                    chave = int(input("Insira uma chave: "))
                    newnode = Node(chave)
                    self.abb.Tree_Insert(newnode)
                    print(f"Nó de chave {newnode.chave} inserido na Árvore com sucesso!")
                else:
                    print("Por favor, crie a Árvore antes de inserir uma chave!")
            elif opc == 3:  # Remover um elemento
                print("\n[> ] Remoção de Chave:")
                if self.abb is not None:
                    chave = int(input("Insira a chave do nó que você quer remover: "))
                    remover_node = self.abb.Iterative_Tree_Search(self.abb.raiz, chave)
                    if remover_node is not None:
                        self.abb.Tree_Delete(remover_node)
                        print(f"Nó de chave {chave} removido da Árvore com sucesso!")
                    else:
                        print(f"Nenhum nó de {chave} encontrado na Árvore!")
                else:
                    print("Por favor, crie a Árvore antes de remover uma chave!")
            elif opc == 4:  # Imprimir a árvore
                print("\n[> ] Imprimir Árvore:")
                if self.abb is not None: 
                    if self.abb.raiz is None:
                        print("Árvore vazia, por favor insira um elemento antes de imprimi-la!")
                    else:
                        formato_impressao = None
                        while formato_impressao != 4:
                            print(">>> Como Deseja Imprimir a Árvore <<<")
                            print("[ 1 ] - In-Order")
                            print("[ 2 ] - Pre-Order")
                            print("[ 3 ] - Post-Order")
                            print("[ 4 ] - Voltar")
                            formato_impressao = int(input("> "))
                            if formato_impressao == 1:
                                print("- Impressão da Árvore In-Order:")
                                self.abb.In_Order_Walk(self.abb.raiz)
                                print()
                            elif formato_impressao == 2:
                                print("- Impressão da Árvore Pre-Order:")
                                self.abb.Pre_Order_Walk(self.abb.raiz)
                                print()
                            elif formato_impressao == 3:
                                print("- Impressão da Árvore Post-Order:")
                                self.abb.Post_Order_Walk(self.abb.raiz)
                                print()
                            else:
                                if formato_impressao != 4:
                                    print("Opção Inválida!")
                else:
                    print("Por favor, crie a Árvore antes de imprimi-la!")
            elif opc == 5:  # Buscar por Chave
                print("\n[> ] Busca de Chave:")
                if self.abb is not None: 
                    chave = int(input("Digite a Chave: "))
                    node_encontrado = self.abb.Iterative_Tree_Search(self.abb.raiz, chave)
                    if node_encontrado is None:
                        print(f"Nenhum nó de valor {chave} encontrado!")
                    else:
                        print(f"Nó de valor {node_encontrado.chave} encontrado!")
                else:
                    print("Por favor, crie a Árvore antes de pesquisar uma chave!")
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

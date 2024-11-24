"""
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
    
    # Método Main
    def main():
        
        # Criando o objeto arvore binaria
        arvore_binaria = BinaryTree()

        # Lista com as chaves a serem inseridas
        chaves = [6, 2, 5, 5, 7, 8]

        # Inserindo as chaves na arvore
        for i in chaves:
            newnode = Node(i)
            arvore_binaria.Tree_Insert(newnode) 
        
        # Printando o conteúdo da arvore
        print("-> Printando a Arvore In-Order: ")
        arvore_binaria.In_Order_Walk(arvore_binaria.raiz)
        print()

        # Buscando um valor na arvore binaria
        print("-> Printando os valores encontrados de 1 - 10: ")
        valores_encontrados = list()
        for i in range(1, 11):
            valor_encontrado = arvore_binaria.Iterative_Tree_Search(arvore_binaria.raiz, i)
            valores_encontrados.append(valor_encontrado)
        for x in valores_encontrados:
            if x != None:
                print(x.chave)
        

        remover_node = arvore_binaria.Iterative_Tree_Search(arvore_binaria.raiz, 5)
        if remover_node is not None:
            arvore_binaria.Tree_Delete(remover_node)
            print("Valor 5 removido com sucesso!")
        else:
            print("Valor 5 não encontrado para remoção!")
        

        # Printando o conteúdo da arvore novamente (In-Order)
        print("-> Printando a Arvore In-Order novamente:")
        arvore_binaria.In_Order_Walk(arvore_binaria.raiz)
        print()


# Chamando a Função Main
Main.main()
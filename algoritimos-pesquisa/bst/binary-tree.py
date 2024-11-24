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
    def inserir(self, valor):
        novo_no = Node(valor)  # Criando o novo nó com a chave fornecida

        if self.raiz is None:
            # Caso especial: a árvore está vazia, então o novo nó se torna a raiz
            self.raiz = novo_no
            return

        # Percorrendo a árvore para encontrar o local correto
        no_atual = self.raiz
        pai = None
        while no_atual:
            pai = no_atual  # Mantém referência ao nó pai
            if valor < no_atual.chave:
                # Ir para a subárvore esquerda
                no_atual = no_atual.esquerda
            else:
                # Ir para a subárvore direita
                no_atual = no_atual.direita

        # Inserindo o novo nó como filho esquerdo ou direito do pai
        if valor < pai.chave:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no
        novo_no.p = pai  # Atualizando a referência ao nó pai


    # Função para percorrer e printar os elementos da arvore (In-Order)
    def In_Order_Walk(self, x):
        if x is not None:
            self.In_Order_Walk(x.esquerda)
            print(x.chave, end=' ')
            self.In_Order_Walk(x.direita)


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
            arvore_binaria.inserir(i) 
        
        # Printando o conteúdo da arvore
        arvore_binaria.In_Order_Walk(arvore_binaria.raiz)
        print()


# Chamando a Função Main
Main.main()
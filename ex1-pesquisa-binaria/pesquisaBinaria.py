
# Criação da estrutura nó
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Criação da estrutura arvore
class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self.inserir_recursivo(self.root, valor)

    def inserir_recursivo(self, atual, valor):
        # Se o valor atual for menor que 
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = Node(valor)
            
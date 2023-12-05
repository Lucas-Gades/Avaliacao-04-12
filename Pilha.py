class Pilha:
    def __init__(self):
        self.top = None
        self.tamanho = 0

    def add(self, veiculo):
        veiculo.proximo = self.top
        self.top = veiculo
        self.tamanho += 1
        self.imprimir()

    def remover(self):
        if self.top is not None:
            self.top = self.top.proximo
            self.tamanho -= 1
            self.imprimir()
        else:
            print("Pilha vazia")

    def imprimir(self):
        if self.top is None:
            print("Pilha Vazia")
        else:
            aux = self.top
            while aux is not None:
                aux.imprimir()
                aux = aux.proximo
            print("Tamanho da Pilha:", self.tamanho)

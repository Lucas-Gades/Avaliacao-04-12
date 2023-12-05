from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        self._qtdHelices = qtdHelices
        self.proximo = None

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Quantidade de hélices:", self._qtdHelices)

    def getQtdHelices(self):
        return self._qtdHelices

    def setQtdHelices(self, qtdHelices):
        self._qtdHelices = qtdHelices


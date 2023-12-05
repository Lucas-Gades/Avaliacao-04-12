from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
        self.proximo = None

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Portas:", self.__portas)

    def getPortas(self):
        return self.__portas

    def setPortas(self, portas):
        self.__portas = portas
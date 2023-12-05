from Carro import Carro
from Drone import Drone
from Pilha import Pilha

def menu():
    print("\nMenu:")
    print("1. Adicionar Carro")
    print("2. Remover Carro")
    print("3. Adicionar Drone")
    print("4. Remover Drone")
    print("5. Imprimir Pilha de Carros")
    print("6. Imprimir Pilha de Drones")
    print("0. Sair")

if __name__ == "__main__":
    pilha_carros = Pilha()
    pilha_drones = Pilha()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            marca = input("Marca do Carro: ")
            modelo = input("Modelo do Carro: ")
            portas = int(input("Número de Portas: "))
            carro = Carro(marca, modelo, portas)
            pilha_carros.add(carro)

        elif escolha == "2":
            pilha_carros.remover()

        elif escolha == "3":
            marca = input("Marca do Drone: ")
            modelo = input("Modelo do Drone: ")
            qtd_helices = int(input("Quantidade de Hélices: "))
            drone = Drone(marca, modelo, qtd_helices)
            pilha_drones.add(drone)

        elif escolha == "4":
            pilha_drones.remover()

        elif escolha == "5":
            pilha_carros.imprimir()

        elif escolha == "6":
            pilha_drones.imprimir()

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def agregar(self, valor):
        self.elementos.append(valor)
    
    def buscar(self, valor):
        return valor in self.elementos

def mostrar_menu():
    print("1. Elegir Cola A")
    print("2. Elegir Cola B")
    print("3. Ingresar cliente")
    print("4. Atender cliente")
    print("5. Salir")

def main():
    cola_a = Cola()
    cola_b = Cola()
    cola_elegida = None
    
    while True:
        mostrar_menu()
        opcion = input("\nPara iniciar elija primero la cola para realizar el ingreso o atencion del cliente\n ")

        if opcion == '1':
            cola_elegida = cola_a
            print("Cola 1 elegida.")
        elif opcion == '2':
            cola_elegida = cola_b
            print("Cola 2 elegida.")
        elif opcion == '3':
            if cola_elegida is None:
                print("Primero debe elegir una cola.")
            else:
                valor = input("Ingrese el numero de atencion del cliente : ")
                cola_elegida.agregar(valor)
                print(f"Valor '{valor}' agregado a la cola {cola_elegida}.")
        elif opcion == '4':
            if cola_elegida is None:
                print("Primero debe elegir una cola.")
            else:
                valor_buscar = input("Ingrese el numero de atencion del cliente: ")
                if cola_elegida.buscar(valor_buscar):
                    print(f"el cliente con el numero '{valor_buscar}' fue atendido.")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

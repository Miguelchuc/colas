from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def agregar(self, valor):
        self.elementos.append(valor)
    
    def atender(self, valor):
        if valor in self.elementos:
            self.elementos.remove(valor)
            return True
        return False
    
    def __str__(self):
        return f"[ {' , '.join(self.elementos)} ]"

def mostrar_menu_principal():
    print("1. Elegir Cola A")
    print("2. Elegir Cola B")
    print("3. Salir")

def mostrar_menu_colas():
    print("1. Ingresar cliente")
    print("2. Atender cliente")
    print("3. Volver al menú principal")

def main():
    cola_a = Cola()
    cola_b = Cola()
    cola_elegida = None
    
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            cola_elegida = cola_a
            print("\nCola A elegida.")
        elif opcion == '2':
            cola_elegida = cola_b
            print("\nCola B elegida.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        while True:
            mostrar_menu_colas()
            opcion_colas = input("\nSeleccione una opción para la cola elegida: ")

            if opcion_colas == '1':
                valor = input("Ingrese el numero de atencion del cliente: ")
                cola_elegida.agregar(valor)
                print(f"Valor '{valor}' agregado a la cola: {cola_elegida}.")
            elif opcion_colas == '2':
                valor_buscar = input("Ingrese el numero de atencion del cliente a atender: ")
                if cola_elegida.atender(valor_buscar):
                    print(f"\nel cliente con el numero '{valor_buscar}' fue atendido.")
                    print(f"Estado actual de la cola: {cola_elegida}.")
                else:
                    print(f"\nel cliente con el numero '{valor_buscar}' no se encuentra en la cola.")
            elif opcion_colas == '3':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

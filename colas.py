class Cola:
    def __init__(self):
        self.cola_A = []  
        self.cola_B = []  

    def agregar_a(self, valor):
        self.cola_A.append(valor)  

    def agregar_b(self, valor):
        self.cola_B.append(valor)

    def vaciar_a(self):
        return self.cola_A.pop(0) if self.cola_A else None

    def vaciar_b(self):
        return self.cola_B.pop(0) if self.cola_B else None

def sumar_colas(cola1, cola2):
    cola_f = Cola()
    print("\nCola A:", cola1.cola_A)
    print("Cola B:", cola2.cola_B)
    
    print("\nSumas de elementos:")
    while cola1.cola_A and cola2.cola_B:
        a = cola1.vaciar_a()
        b = cola2.vaciar_b()
        suma = a + b
        cola_f.agregar_a(suma)  
        print(f"Sumando {a} + {b} = {suma}")
        
        
        print("Cola A:", cola1.cola_A)
        print("Cola B:", cola2.cola_B)
    
    return cola_f

if __name__ == "__main__":
    cola1 = Cola()
    cola2 = Cola()

    T = int(input("Ingresa el tamaño de las colas: "))

    print("Ingrese los elementos para la Cola A:")
    for i in range(T):
        num = int(input(f"Ingrese el elemento {i + 1}: "))
        cola1.agregar_a(num)
    
    print("Ingrese los elementos para la Cola B:")
    for i in range(T):
        num = int(input(f"Ingrese el elemento {i + 1}: "))
        cola2.agregar_b(num)
    
    
    resultado_cola = sumar_colas(cola1, cola2)
    
    print("\nCola Resultado:")
    for elemento in resultado_cola.cola_A:  
        print(elemento)

class Cola:
    def __init__(self):
        self.cola_A = []  
        self.cola_B = []  

    def agregar_a(self, valor):
        self.cola_A.append(valor)  

    def agregar_b(self, valor):
        self.cola_B.append(valor)

    def sum(self):
        self.cola_resultado = []
        for a, b in zip(self.cola_A, self.cola_B):
            self.cola_resultado.append(a + b)
        return self.cola_resultado

if __name__ == "__main__":
    cola = Cola()

T=int(input("ingresa el tamaño de las colas"))

print("Ingrese los elementos para la Cola A:")
for i in range(T):
    num = int(input(f"Ingrese el elemento {i + 1}: "))
    cola.agregar_a(num)

    
print("Ingrese los elementos para la Cola B:")
for i in range(T):
    num = int(input(f"Ingrese el elemento {i + 1}: "))
    cola.agregar_b(num)

    
resultado = [cola.sum()]    
print("Cola Resultado:")
for elemento in resultado:
    print(elemento)
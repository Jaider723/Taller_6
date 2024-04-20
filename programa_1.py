class Figura:
    def __init__(self):
        self._area = 0

    def area(self):
        return self._area

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.set_radio(radio)

    def set_radio(self, radio):
        if radio > 0:
            self._radio = radio
            self._area = 3.1416 * (radio ** 2)
        else:
            raise ValueError("El radio debe ser un número positivo")

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.set_lado(lado)

    def set_lado(self, lado):
        if lado > 0:
            self._lado = lado
            self._area = lado * lado
        else:
            raise ValueError("El lado debe ser un número positivo")

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        super().__init__()
        self.set_dimensiones(largo, ancho)

    def set_dimensiones(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self._largo = largo
            self._ancho = ancho
            self._area = largo * ancho
        else:
            raise ValueError("Las dimensiones deben ser números positivos")

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.set_base_altura(base, altura)

    def set_base_altura(self, base, altura):
        if base > 0 and altura > 0:
            self._base = base
            self._altura = altura
            self._area = (base * altura) / 2
        else:
            raise ValueError("La base y la altura deben ser números positivos")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Calcular área de un círculo")
        print("2. Calcular área de un cuadrado")
        print("3. Calcular área de un rectángulo")
        print("4. Calcular área de un triángulo")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"Área del círculo: {circulo.area()}")
        elif opcion == '2':
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"Área del cuadrado: {cuadrado.area()}")
        elif opcion == '3':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.area()}")
        elif opcion == '4':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            triangulo = Triangulo(base, altura)
            print(f"Área del triángulo: {triangulo.area()}")
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()


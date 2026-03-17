import math

class Geometrico:
    def __init__(self, figura):
        self.figura = figura

    def calcular_area(self):

        if self.figura == "quadrado":
            lado = float(input("Digite o lado do quadrado: "))
            area = lado ** 2
            print("Área do quadrado:", area)

        elif self.figura == "retangulo":
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            area = base * altura
            print("Área do retângulo:", area)

        elif self.figura == "circulo":
            raio = float(input("Digite o raio do círculo: "))
            area = math.pi * raio ** 2
            print("Área do círculo:", area)

        else:
            print("Figura inválida")

figura = input("Digite a forma geométrica (quadrado, retangulo ou circulo): ")

forma = Geometrico(figura)
forma.calcular_area()
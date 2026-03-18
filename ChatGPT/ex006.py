class Retangulo:
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return f"A área é de {self.largura * self.altura}."
        
    def perimetro(self):
        return f"O perímetro é de {2 * (self.largura + self.altura)}"
        
c1 = Retangulo(10, 5)
print(c1.area())
print(c1.perimetro())

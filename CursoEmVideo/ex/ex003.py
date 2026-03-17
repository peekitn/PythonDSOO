class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(f"Nome: {self.nome}")
        print(f"Preco: {self.preco}")

c1 = Produto(nome = "Iphone", preco = 1500)
c1.etiqueta()


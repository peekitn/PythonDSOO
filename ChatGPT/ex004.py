class Produto:
    def __init__(self, preco):
        self._preco = preco
        
    def get_preco(self):
        return self._preco
    
    def set_preco(self, novo_preco):
        if novo_preco < 0:
            print("Preço não pode ser negativo.")
        else:
            self._preco = novo_preco

# Teste
c1 = Produto(15)
print(c1.get_preco())  # 15
c1.set_preco(30)
print(c1.get_preco())  # 30
c1.set_preco(-10)  # erro

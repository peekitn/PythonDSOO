# Declaracao de Classes
class pessoa:
    def __init__(self, nome=""): # Metodo Construtor
        # Atributos de Instancia
        self.__nome = nome

@property
def nome(self):
    return self.__nome

@nome.setter
def nome(self, nome):
    self.__nome = nome

p1 = pessoa("peekitn")
p1.nome = "Anderson"
print(p1.nome)
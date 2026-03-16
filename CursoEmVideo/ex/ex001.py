# Declaracao de Classes
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto que eh uma pessoa que tem nome e idade

    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Metodo Construtor
    # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    #Metodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1 #self.idade += 1

    def mensagem(self):
        return f"{self.nome} eh Gafanhoto e tem {self.idade} anos de idade."
    
    def __str__(self): # Dunder Method
        return "Vou te mostrar uma coisa..."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
# Declaracao de Objetos
g1 = Gafanhoto(nome = "Maria", idade = 17)
g1.aniversario()
print(g1.mensagem())
#  print(g1.__doc__) # Dunder Attribute
print(g1.__getstate__())
# print(g1)
print(g1.__class__)

g2 = Gafanhoto(nome = "Mauro", idade = 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())


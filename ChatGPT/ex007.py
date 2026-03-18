class Animal:
    def __init__(self, especie):
        self.especie = especie
        
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
        return "AuAu"
        
class Gato(Animal):
    def fazer_som(self):
        return "Miau"
    
c = Cachorro("Canino")
g = Gato("Felino")

print(c.fazer_som())  # Au au
print(g.fazer_som())  # Miau

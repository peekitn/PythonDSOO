class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"Livro: {self.titulo} por {self.autor}"
        
c1 = Livro("Watchmen", "Alan Moore")
print(c1)

class Livro:
    def __init__(self, titulo, pagina_atual, paginas):
        self.titulo = titulo
        self.pagina_atual = pagina_atual
        self.paginas = paginas

    def virar_pagina(self):
        if self.pagina_atual < self.paginas:
            self.pagina_atual += 1
            print(f"Agora voce esta na pagina {self.pagina_atual}")
        else:
            print("Voce ja chegou ao fim da leitura.")

c1 = Livro(titulo = "Cortella", pagina_atual = 38, paginas = 40)
c1.virar_pagina()

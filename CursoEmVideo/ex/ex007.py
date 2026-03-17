class ControleRemoto:
    def __init__(self, canal, volume, estado):
        self.canal = canal
        self.volume = volume
        self.estado = estado

    def inserir_canal(self):
        print(f"Voce inseriu no canal {self.canal}")
    
    def nivel_volume(self):
        print(f"Voce inseriu o volume no nivel {self.volume}")

    def mostrar_estado(self):
        print(f"Voce optou por {self.estado}")

c1 = ControleRemoto(canal = "HBO", volume = 78, estado = "Ligado")
c1.inserir_canal()
c1.nivel_volume()
c1.mostrar_estado()
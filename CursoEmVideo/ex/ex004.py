class Churrasco:
    def __init__(self, qtd_pss, consumo_carne, preco_kg):
        self.qtd_pss = qtd_pss
        self.consumo_carne = consumo_carne
        self.preco_kg = preco_kg

    def analisar(self):
        carne_total = self.qtd_pss * self.consumo_carne
        custo_total = carne_total * self.preco_kg
        preco_por_pessoa = custo_total / self.qtd_pss

        print(f"Vão participar {self.qtd_pss} pessoas.")
        print(f"Comprar {carne_total:.2f} kg de carne.")
        print(f"Custo total: R$ {custo_total:.2f}")
        print(f"Preço por pessoa: R$ {preco_por_pessoa:.2f}")

c1 = Churrasco(qtd_pss=15, consumo_carne=0.4, preco_kg=82.40)
c1.analisar()
class Gamer:
    def __init__(self, nome, nick, jgs_favs):
        self.nome = nome
        self.nick = nick
        self.jgs_favs = jgs_favs

    def mostra_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Nick: {self.nick}")
        print(f"Jogos Favoritos:")
        for jogo in self.jgs_favs:
            print("-", jogo)

c1 = Gamer(nome = "Alexandre", nick = "peekitn", jgs_favs = ["Resident Evil 7", "Resident Evil Revelations"])
c1.mostra_ficha()
class Musica:
    def __init__(self, faixa: int, titulo: str):
        self.__faixa = faixa
        self.__titulo = titulo

    @property
    def faixa(self):
        return self.__faixa

    @faixa.setter
    def faixa (self, faixa):
        self.__faixa = faixa

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
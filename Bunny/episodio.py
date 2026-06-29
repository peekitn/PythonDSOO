class Episodio:
    def __init__(self, numero: int, titulo: str, duracao_minutos: int):
        self.__numero = numero
        self.__titulo = titulo
        self.__duracao_minutos = duracao_minutos
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def duracao_minutos(self):
        return self.__duracao_minutos
    
    @duracao_minutos.setter
    def duracao_minutos(self, duracao_minutos):
        self.__duracao_minutos = duracao_minutos
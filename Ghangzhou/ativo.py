class Ativo:
    def __init__(self, codigo: int, nome: str, valor_investido: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__valor_investido = valor_investido

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor_investido(self):
        return self.__valor_investido
    
    @valor_investido.setter
    def valor_investido(self, valor_investido):
        self.__valor_investido = valor_investido


    
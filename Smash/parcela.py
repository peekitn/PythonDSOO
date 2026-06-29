class Parcela:
    def __init__(self, codigo: int, valor_principal: float, valor_juros: float):
        self.__codigo = codigo
        self.__valor_principal = valor_principal
        self.__valor_juros = valor_juros

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def valor_principal(self):
        return self.__valor_principal
    
    @valor_principal.setter
    def valor_principal(self, valor_principal):
        self.__valor_principal = valor_principal

    @property
    def valor_juros(self):
        return self.__valor_juros
    
    @valor_juros.setter
    def valor_juros(self, valor_juros):
        self.__valor_juros = valor_juros
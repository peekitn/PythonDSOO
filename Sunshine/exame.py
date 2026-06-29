class Exame:
    def __init__(self, codigo: int, descricao: str, custo: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__custo = custo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo
    
    @custo.setter
    def custo(self, custo):
        self.__custo = custo
class Componente:
    def __init__(self, codigo: int, descricao: str, preco_base: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_base = preco_base

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
    def preco_base(self):
        return self.__preco_base
    
    @preco_base.setter
    def preco_base(self, preco_base):
        self.__preco_base = preco_base
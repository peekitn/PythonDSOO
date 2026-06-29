class Requisicao:
    def __init__(self, codigo: int, prompt: str, custo_base: float):
        self.__codigo = codigo
        self.__prompt = prompt
        self.__custo_base = custo_base

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def prompt(self):
        return self.__prompt
    
    @prompt.setter
    def prompt(self, prompt):
        self.__prompt = prompt

    @property
    def custo_base(self):
        return self.__custo_base
    
    @custo_base.setter
    def custo_base(self, custo_base):
        self.__custo_base = custo_base
class Medico:
    def __init__(self, crm: str, nome: str, valor_consulta: float):
        self.__crm = crm
        self.__nome = nome
        self.__valor_consulta = valor_consulta

    @property
    def crm(self):
        return self.__crm
    
    @crm.setter
    def crm(self, crm):
        self.__crm = crm

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor_consulta(self):
        return self.__valor_consulta
    
    @valor_consulta.setter
    def valor_consulta(self, valor_consulta):
        self.__valor_consulta = valor_consulta
class ModeloAI:
    def __init__(self, nome: str, fator_computacional: float):
        self.__nome = nome
        self.__fator_computacional = fator_computacional

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def fator_computacional(self):
        return self.__fator_computacional
    
    @fator_computacional.setter
    def fator_computacional(self, fator_computacional):
        self.__fator_computacional = fator_computacional
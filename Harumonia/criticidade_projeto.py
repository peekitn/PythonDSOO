class CriticidadeProjeto:
    def __init__(self, descricao: str, fator_urgencia: float):
        self.__descricao = descricao
        self.__fator_urgencia = fator_urgencia

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def fator_urgencia(self):
        return self.__fator_urgencia
    
    @fator_urgencia.setter
    def fator_urgencia(self, fator_urgencia):
        self.__fator_urgencia = fator_urgencia
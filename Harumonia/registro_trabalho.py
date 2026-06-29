class RegistroTrabalho:
    def __init__(self, codigo: int, horas_trabalhadas: int, indice_stress: float):
        self.__codigo = codigo
        self.__horas_trabalhadas = horas_trabalhadas
        self.__indice_stress = indice_stress

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas_trabalhadas):
        self.__horas_trabalhadas = horas_trabalhadas

    @property
    def indice_stress(self):
        return self.__indice_stress
    
    @indice_stress.setter
    def indice_stress(self, indice_stress):
        self.__indice_stress = indice_stress
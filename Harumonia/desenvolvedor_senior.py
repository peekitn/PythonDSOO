from desenvolvedor import Desenvolvedor

class DesenvolvedorSenior(Desenvolvedor):
    def __init__(self, bonus_lideranca: float, cpf: str, nome: str, valor_hora: float):
        super().__init__(cpf, nome, valor_hora)
        self.__bonus_lideranca = bonus_lideranca

    @property
    def bonus_lideranca(self):
        return self.__bonus_lideranca
    
    @bonus_lideranca.setter
    def bonus_lideranca(self, bonus_lideranca):
        self.__bonus_lideranca = bonus_lideranca

    
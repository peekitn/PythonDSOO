from passagem_duplicada_exception import PassagemDuplicadaException
from passagem import Passagem

class CompanhiaAerea:
    def __init__(self):
        self.__passagens = []
        # Inicializar a lista de passagens vazia aqui
    @property
    def passagens(self):
        return self.__passagens
    
    @passagens.setter
    def passagens(self, passagens):
        self.__passagens = passagens
    # Getter e Setter para passagens

    '''
    Busca passagem pelo localizador. Retorna None se não encontrar.
    '''
    def busca_passagem_por_localizador(self, localizador: int):
        if localizador is None:
            return None
        
        for passagem in self.passagens:
            if passagem.localizador == localizador:
                return passagem
            
        return None

    '''
    Adiciona a passagem. Levanta PassagemDuplicadaException se o localizador ja existir.
    '''
    def incluir_passagem(self, passagem: Passagem):
        if passagem is None:
            return None
        
        if self.busca_passagem_por_localizador(passagem.localizador) is not None:
            raise PassagemDuplicadaException()
        self.__passagens.append(passagem)

    '''
    Remove pelo localizador e retorna a passagem. Retorna None se nao achar.
    '''
    def excluir_passagem(self, localizador: int):
        if localizador is None:
            return None
        passagem = self.busca_passagem_por_localizador(localizador)
        if passagem is None:
            return None
        self.__passagens.remove(passagem)
        return passagem

    '''
    Soma o valor total de TODAS as passagens registradas no controlador.
    Retorna float.
    '''
    def calcular_faturamento_total(self):
        total = sum(passagem.calcular_valor_total() for passagem in self.__passagens)
        return float(total)
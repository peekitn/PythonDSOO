from sessao_duplicada_exception import SessaoDuplicadaException
from sessao_geracao import SessaoGeracao

class PlataformaArteAI:
    def __init__(self):
        self.__sessoes = []
        # Inicializar a lista de sessoes vazia aqui
    @property
    def sessoes(self):
        return self.__sessoes
    
    @sessoes.setter
    def sessoes(self, sessoes):
        self.__sessoes = sessoes
    # Getter e Setter para sessoes

    '''
    Busca sessao pelo codigo. Retorna None se nao encontrar.
    '''
    def busca_sessao_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for sessao in self.__sessoes:
            if sessao.codigo == codigo:
                return sessao
            
        return None

    '''
    Adiciona a sessao. Levanta SessaoDuplicadaException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_sessao(self, sessao: SessaoGeracao):
        if sessao is None or not isinstance(sessao, SessaoGeracao):
            return
        
        if self.busca_sessao_por_codigo(sessao.codigo) is not None:
            raise SessaoDuplicadaException()

        self.__sessoes.append(sessao)

    '''
    Remove pelo codigo e retorna a sessao. Retorna None se nao achar.
    '''
    def excluir_sessao(self, codigo: int):
        if codigo is None:
            return None
        
        sessao_excluida = self.busca_sessao_por_codigo(codigo)
        if sessao_excluida is None:
            return None
        
        self.__sessoes.remove(sessao_excluida)
        return sessao_excluida

    '''
    Soma o custo total de TODAS as sessoes realizadas pelo usuario com o cpf passado por parametro.
    Retorna float.
    '''
    def calcular_gasto_por_cpf(self, cpf: str):
        total_gasto = 0.0
        for sessao in self.__sessoes:
            # Filtra pelo CPF passado por parametro
            if sessao.usuario.cpf == cpf:
                total_gasto += sessao.calcular_custo_total()
                
        return float(total_gasto)
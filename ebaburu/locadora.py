from locacao_duplicada_exception import LocacaoDuplicadaException
from locacao import Locacao

class Locadora:
    def __init__(self):
        self.__locacoes = []
        # Inicializar a lista de locacoes vazia aqui
    @property
    def locacoes(self):
        return self.__locacoes
    
    @locacoes.setter
    def locacoes(self, locacoes):
        self.__locacoes = locacoes
    # Getter e Setter para locacoes

    '''
    Busca locacao pelo codigo. Retorna None se não encontrar.
    '''
    def busca_locacao_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for locacao in self.__locacoes:
            if locacao.codigo == codigo:
                return locacao
        return None

    '''
    Adiciona a locacao. Levanta LocacaoDuplicadaException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_locacao(self, locacao: Locacao):
        if locacao is None or not isinstance(locacao, Locacao):
            return
        
        if self.busca_locacao_por_codigo(locacao.codigo) is not None:
            raise LocacaoDuplicadaException()
        
        self.__locacoes.append(locacao)

    '''
    Remove pelo codigo e retorna a locacao. Retorna None se nao achar.
    '''
    def excluir_locacao(self, codigo: int):
        if codigo is None:
            return None
        
        locacao_excluida = self.busca_locacao_por_codigo(codigo) 
        if locacao_excluida is None:
            return None
            
        self.__locacoes.remove(locacao_excluida)
        return locacao_excluida

    '''
    Soma o valor total de TODAS as locacoes realizadas pelo cliente com o cpf passado por parametro.
    Retorna float.
    '''
    def calcular_faturamento_por_cpf(self, cpf: str):
        if cpf is None:
            return 0.0
            
        faturamento_total = 0.0
        for locacao in self.__locacoes:
            # Verifica se o CPF do cliente da locacao eh o mesmo que estamos buscando
            if locacao.cliente.cpf == cpf:
                faturamento_total += locacao.calcular_valor_locacao()
                
        return float(faturamento_total)
from carteira_duplicada_exception import CarteiraDuplicadaException
from carteira import Carteira

class Banco:
    def __init__(self):
        self.__carteiras = []
        # Inicializar a lista de carteiras vazia aqui

    # Getter e Setter para carteiras
    @property
    def carteiras(self):
        return self.__carteiras
    
    @carteiras.setter
    def carteiras(self, carteiras):
        self.__carteiras = carteiras
    '''
    Busca carteira pelo numero. Retorna None se não encontrar.
    '''
    def busca_carteira_por_numero(self, numero: int):
        if numero is None:
            return None
        
        for carteira in self.__carteiras:
            if carteira.numero == numero:
                return carteira
        return None

    '''
    Adiciona a carteira. Levanta CarteiraDuplicadaException se o numero ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_carteira(self, carteira: Carteira):
        if carteira is None:
            return None
        
        if self.busca_carteira_por_numero(carteira.numero) is not None:
            raise CarteiraDuplicadaException()
        
        self.__carteiras.append(carteira)

    '''
    Remove pelo numero e retorna a carteira. Retorna None se nao achar.
    '''
    def excluir_carteira(self, numero: int):
        if numero is None:
            return None
        
        for carteira in self.__carteiras:
            if carteira.numero == carteira:
                self.__carteiras.remove(carteira)
                return carteira

    '''
    Soma o saldo total de TODAS as carteiras que pertencem ao cpf passado como parametro.
    Retorna float.
    '''
    def calcular_capital_sob_gestao(self, cpf: str):
        total = 0.0
        for carteira in self.__carteiras:
            # Verifica se a carteira pertence ao cpf procurado
            if carteira.cliente.cpf == cpf:
                total += carteira.calcular_saldo_total()
        return float(total)
from reserva_duplicada_exception import ReservaDuplicadaException
from reserva import Reserva

class Hotel:
    def __init__(self):
        self.__reservas = []
        # Inicializar a lista de reservas vazia aqui
    @property
    def reservas(self):
        return self.__reservas
    
    @reservas.setter
    def reservas(self, reservas):
        self.__reservas = reservas
    # Getter e Setter para reservas

    '''
    Busca reserva pelo codigo. Retorna None se não encontrar.
    '''
    def busca_reserva_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for reserva in self.__reservas:
            if reserva.codigo == codigo:
                return reserva
        return None

    '''
    Adiciona a reserva. Levanta ReservaDuplicadaException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_reserva(self, reserva: Reserva):
        if reserva is None or not isinstance(reserva, Reserva):
            return
        
        if self.busca_reserva_por_codigo(reserva.codigo) is not None:
            raise ReservaDuplicadaException()
        
        self.__reservas.append(reserva)

    '''
    Remove pelo codigo e retorna a reserva. Retorna None se nao achar.
    '''
    def excluir_reserva(self, codigo: int):
        if codigo is None:
            return None
        
        reserva_excluida = self.busca_reserva_por_codigo(codigo)
        if reserva_excluida is None:
            return None
        
        self.__reservas.remove(reserva_excluida)
        return reserva_excluida

    '''
    Soma o valor total de TODAS as reservas realizadas pelo hospede com o cpf passado por parametro.
    Retorna float.
    '''
    def calcular_faturamento_por_cpf(self, cpf: str):
        if cpf is None:
            return 0.0
            
        total = 0.0
        for reserva in self.__reservas:
            if reserva.hospede.cpf == cpf:
                total += reserva.calcular_valor_total()
                
        return float(total)
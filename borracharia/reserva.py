from hospede import Hospede
from quarto import Quarto
from consumo import Consumo
from hospede_vip import HospedeVIP

class Reserva:
    def __init__(self, codigo: int, dias: int, hospede: Hospede, quarto: Quarto):
        self.__codigo = codigo
        self.__dias = dias
        self.__hospede = hospede
        self.__quarto = quarto
        self.__consumos = []
        # Inicializar a lista de consumos vazia aqui
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def dias(self):
        return self.__dias
    
    @dias.setter
    def dias(self, dias):
        self.__dias = dias

    @property
    def hospede(self):
        return self.__hospede
    
    @hospede.setter
    def hospede(self, hospede):
        self.__hospede = hospede

    @property
    def quarto(self):
        return self.__quarto
    
    @quarto.setter
    def quarto(self, quarto):
        self.__quarto = quarto

    @property
    def consumos(self):
        return self.__consumos
    
    @consumos.setter
    def consumos(self, consumos):
        self.__consumos = consumos

    # Getters e Setters para codigo, dias, hospede e quarto
    # Getter e Setter para consumos

    '''
    Inclui um novo consumo na lista. Retorna o consumo se sucesso, None se o codigo ja existir.
    '''
    def incluir_consumo(self, codigo: int, descricao: str, preco: float):
        if codigo is None or descricao is None or preco is None:
            return None
        
        for consumo in self.__consumos:
            if consumo.codigo == codigo:
                return None
            
        novo_consumo = Consumo(codigo, descricao, preco)
        self.__consumos.append(novo_consumo)
        return novo_consumo

    '''
    Exclui o consumo pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_consumo(self, codigo: int):
        if codigo is None:
            return None
        
        for consumo in self.__consumos:
            if consumo.codigo == codigo:
                self.__consumos.remove(consumo)
                return consumo
        return None

    '''
    Multiplica a quantidade de dias da reserva pelo valor_diaria do quarto.
    Soma o preco de TODOS os consumos presentes na reserva a esse valor das diarias.
    Se o hospede for HospedeVIP, calcula o desconto multiplicando o percentual_desconto 
    pelo valor total atual, e subtrai esse desconto do valor final.
    Retorna float.
    '''
    def calcular_valor_total(self):
        # Multiplica os dias pelo valor da diaria
        total_diarias = self.__dias * self.__quarto.valor_diaria
        
        # Soma o preco de todos os consumos extras
        total_consumos = sum(consumo.preco for consumo in self.__consumos)
        
        valor_final = total_diarias + total_consumos

        # Valida heranca e aplica desconto se for VIP
        if isinstance(self.__hospede, HospedeVIP):
            desconto = valor_final * self.__hospede.percentual_desconto
            valor_final -= desconto

        return float(valor_final)
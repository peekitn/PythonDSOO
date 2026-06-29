from passageiro import Passageiro
from voo import Voo
from bagagem import Bagagem
from passageiro_frequente import PassageiroFrequente

class Passagem:
    def __init__(self, localizador: int, passageiro: Passageiro, voo: Voo):
        self.__localizador = localizador
        self.__passageiro = passageiro
        self.__voo = voo
        self.__bagagens = []
        # Inicializar a lista de bagagens vazia aqui
    
    @property
    def localizador(self):
        return self.__localizador
    
    @localizador.setter
    def localizador(self, localizador):
        self.__localizador = localizador

    @property
    def passageiro(self):
        return self.__passageiro
    
    @passageiro.setter
    def passageiro(self, passageiro):
        self.__passageiro = passageiro

    @property
    def voo(self):
        return self.__voo
    
    @voo.setter
    def voo(self, voo):
        self.__voo = voo

    @property
    def bagagens(self):
        return self.__bagagens
    
    @bagagens.setter
    def bagagens(self, bagagens):
        self.__bagagens = bagagens
    # Getters e Setters para localizador, passageiro e voo
    # Getter para bagagens

    '''
    Inclui uma nova bagagem na lista. Retorna a bagagem se sucesso, None se o codigo ja existir.
    '''
    def incluir_bagagem(self, codigo: int, peso: float, preco_extra: float):
        if codigo is None or peso is None or preco_extra is None:
            return None
        
        for bagagem in self.__bagagens:
            if bagagem.codigo == codigo:
                return None
            
        bagagem_novo = Bagagem(codigo, peso, preco_extra)
        self.__bagagens.append(bagagem_novo)
        return bagagem_novo

    '''
    Exclui a bagagem pelo codigo e a retorna. Retorna None se nao achar.
    '''
    def excluir_bagagem(self, codigo: int):
        if codigo is None:
            return None
        for bagagem in self.__bagagens:
            if bagagem.codigo == codigo:
                self.__bagagens.remove(bagagem)
                return bagagem
        return None

    '''
    Soma o preco_base do voo com o preco_extra de TODAS as bagagens.
    Se o passageiro for PassageiroFrequente, subtrai o desconto percentual do valor total calculado.
    Retorna float.
    '''
    def calcular_valor_total(self):
        total = self.__voo.preco_base
        total_bagagens = sum(bagagem.preco_extra for bagagem in self.__bagagens)
        total += total_bagagens
        if isinstance(self.__passageiro, PassageiroFrequente):
            total -= (total * self.__passageiro.desconto)
            
        return float(total)
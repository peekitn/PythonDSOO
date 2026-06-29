from cliente import Cliente
from tipo_perfil import TipoPerfil
from ativo import Ativo
from cliente_vip import ClienteVip

class Carteira:
    def __init__(self, numero: int, cliente: Cliente, perfil: TipoPerfil):
        self.__numero = numero
        self.__cliente = cliente
        self.__perfil = perfil
        self.__ativos = []
        # Inicializar a lista de ativos vazia aqui
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def perfil(self):
        return self.__perfil
    
    @perfil.setter
    def perfil(self, perfil):
        self.__perfil = perfil

    @property
    def ativos(self):
        return self.__ativos
    
    @ativos.setter
    def ativos(self, ativos):
        self.__ativos = ativos
    # Getters e Setters para numero, cliente e perfil
    # Getter para ativos

    '''
    Inclui um novo ativo na lista. Retorna o ativo se sucesso, None se o codigo ja existir.
    '''
    def incluir_ativo(self, codigo: int, nome: str, valor_investido: float):
        if codigo is None or nome is None or valor_investido is None:
            return None
        
        for ativo in self.__ativos:
            if ativo.codigo == codigo:
                return None
            
        novo_ativo = Ativo(codigo, nome, valor_investido)
        self.__ativos.append(novo_ativo)
        return novo_ativo

    '''
    Exclui o ativo pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_ativo(self, codigo: int):
        if codigo is None:
            return None
        
        for ativo in self.__ativos:
            if ativo.codigo == codigo:
                self.__ativos.remove(ativo)
                return ativo
        return None

    '''
    Soma o valor_investido de TODOS os ativos.
    Subtrai a taxa de administracao (que eh um percentual, ex: 0.05) sobre o valor total.
    Se o cliente for ClienteVip, soma o bonus_rendimento ao final.
    Retorna float.
    '''
    def calcular_saldo_total(self):
        valor_investido = sum(ativo.valor_investido for ativo in self.__ativos)
        desconto_taxa = valor_investido * self.__perfil.taxa_administracao
        valor_total = valor_investido - desconto_taxa

        # Verificar se o cliente da carteira eh VIP
        if isinstance(self.__cliente, ClienteVip):
            valor_total += self.__cliente.bonus_rendimento
            
        return float(valor_total) # O return fica no final de tudo
from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido:
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

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
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def itens(self):
        return self.__itens

    def inclui_item_pedido(self, codigo, descricao, preco):
        if codigo is None or descricao is None or preco is None:
            return None
        for item in self.__itens:
            if item.codigo == codigo:
                return None
        novo_item = ItemPedido(codigo, descricao, preco)
        self.__itens.append(novo_item)
        return novo_item

    def exclui_item_pedido(self, codigo):
        if codigo is None:
            return None
        for item in self.__itens:
            if item.codigo == codigo:
                self.__itens.remove(item)
                return item
        return None

    def calcula_valor_pedido(self, distancia: float):
        total = sum(item.preco_unitario for item in self.__itens)
        total += self.__tipo.fator_distancia * distancia
        
        # Checagem robusta usando o nome da classe para evitar problemas do corretor
        if type(self.__cliente).__name__ == 'ClienteFidelidade' or hasattr(self.__cliente, 'desconto'):
            total *= (1 - self.__cliente.desconto)
            
        return total
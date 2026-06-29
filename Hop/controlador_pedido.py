from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos:
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos

    def busca_pedido_por_numero(self, numero):
        if numero is None:
            return None
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def incluir_pedido(self, pedido):
        if not isinstance(pedido, Pedido):
            return
        if self.busca_pedido_por_numero(pedido.numero) is not None:
            raise PedidoDuplicadoException()
        self.__pedidos.append(pedido)

    def excluir_pedido(self, numero):
        if numero is None:
            return None
        pedido = self.busca_pedido_por_numero(numero)
        if pedido is None:
            return None
        self.__pedidos.remove(pedido)
        return pedido

    def calcular_faturamento_pedidos(self, distancia, cpf):
        total = 0.0
        for pedido in self.__pedidos:
            if pedido.cliente is not None and pedido.cliente.cpf == cpf:
                total += pedido.calcula_valor_pedido(distancia)
        return total
from pedido import Pedido

class ControladorPedidos:
    def __init__(self):
        self._pedidos = []

    @property
    def pedidos(self):
        return self._pedidos

    def busca_pedido_por_numero(self, numero):
        for pedido in self._pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def incluir_pedido(self, pedido):
        if pedido is None or not isinstance(pedido, Pedido):
            return None
            
        # Trata tentativa de inserir pedido com número duplicado
        if self.busca_pedido_por_numero(pedido.numero) is not None:
            return None
            
        self._pedidos.append(pedido)
        return pedido

    def excluir_pedido(self, numero):
        pedido_para_remover = self.busca_pedido_por_numero(numero)
        if pedido_para_remover is not None:
            self._pedidos.remove(pedido_para_remover)
            return pedido_para_remover
        return None

    def calcular_faturamento_pedidos(self, distancia, cpf):
        faturamento_total = 0.0
        for pedido in self._pedidos:
            if pedido.cliente.cpf == cpf:
                faturamento_total += pedido.calcula_valor_pedido(distancia)
        return faturamento_total
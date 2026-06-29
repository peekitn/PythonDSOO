class PedidoDuplicadoException(Exception):
    def __init__(self, mensagem = "Pedido duplicado."):
        super().__init__(mensagem)
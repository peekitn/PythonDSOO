class PedidoDuplicadoException(Exception):
    def __init__(self, mensagem="Pedido ja cadastrado"):
        super().__init__(mensagem)
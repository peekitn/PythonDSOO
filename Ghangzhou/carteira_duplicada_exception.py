class CarteiraDuplicadaException(Exception):
    def __init__(self, mensagem = "Mensagem"):
        super().__init__(mensagem)
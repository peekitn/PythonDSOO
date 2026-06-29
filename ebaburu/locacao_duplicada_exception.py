class LocacaoDuplicadaException(Exception):
    def __init__(self, mensagem = "Locacao duplicada."):
        super().__init__(mensagem)
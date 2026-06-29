class SessaoDuplicadaException(Exception):
    def __init__(self, mensagem = "Sessao duplicada."):
        super().__init__(mensagem)
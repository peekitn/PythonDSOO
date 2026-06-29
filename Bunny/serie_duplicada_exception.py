class SerieDuplicadaException(Exception):
    def __init__(self, mensagem = "Serie ja foi usada."):
        super().__init__(mensagem)
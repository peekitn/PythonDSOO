class PassagemDuplicadaException(Exception):
    def __init__(self, mensagem = "Passagem ja existe."):
        super().__init__(mensagem)
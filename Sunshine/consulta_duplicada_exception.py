class ConsultaDuplicadaException(Exception):
    def __init__(self, mensagem = "Consula ja existe."):
        super().__init__(mensagem)
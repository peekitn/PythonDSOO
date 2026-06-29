class ProjetoDuplicadoException(Exception):
    def __init__(self, mensagem = "Projeto ja existe."):
        super().__init__(mensagem)
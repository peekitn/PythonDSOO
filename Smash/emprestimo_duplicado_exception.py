class EmprestimoDuplicadoException(Exception):
    def __init__(self, mensagem = "Emprestimo duplicado."):
        super().__init__(mensagem)
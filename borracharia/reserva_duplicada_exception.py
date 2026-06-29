class ReservaDuplicadaException(Exception):
    def __init__(self, mensagem = "Reserva duplicada."):
        super().__init__(mensagem)
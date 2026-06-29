from usuario import Usuario

class UsuarioPro(Usuario):
    def __init__(self, desconto_percentual: float, cpf: str, nome: str, email: str):
        super().__init__(cpf, nome, email)
        self.__desconto_percentual = desconto_percentual

    @property
    def desconto_percentual(self):
        return self.__desconto_percentual
    
    @desconto_percentual.setter
    def desconto_percentual(self, desconto_percentual):
        self.__desconto_percentual = desconto_percentual
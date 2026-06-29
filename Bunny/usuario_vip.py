from usuario import Usuario

class UsuarioVip(Usuario): 
    def __init__(self, telas_simultaneas: int, email: str, nome: str, mensalidade: float):
        super().__init__(email, nome, mensalidade)
        self.__telas_simultaneas = telas_simultaneas
    
    @property
    def telas_simultaneas(self):
        return self.__telas_simultaneas
    
    @telas_simultaneas.setter
    def telas_simultaneas(self, telas_simultaneas):
        self.__telas_simultaneas = telas_simultaneas

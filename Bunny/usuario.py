class Usuario:
    def __init__(self, email: str, nome: str, mensalidade: float):
        self.__email = email
        self.__nome = nome
        self.__mensalidade = mensalidade

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def mensalidade(self):
        return self.__mensalidade
    
    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade
class TipoPerfil:
    def __init__(self, descricao: str, taxa_administracao: float):
        self.__descricao = descricao
        self.__taxa_administracao = taxa_administracao

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def taxa_administracao(self):
        return self.__taxa_administracao
    
    @taxa_administracao.setter
    def taxa_administracao(self, taxa_administracao):
        self.__taxa_administracao = taxa_administracao
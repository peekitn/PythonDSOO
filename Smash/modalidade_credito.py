class ModalidadeCredito:
    def __init__(self, descricao: str, taxa_juros: float):
        self.__descricao = descricao
        self.__taxa_juros = taxa_juros

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def taxa_juros(self):
        return self.__taxa_juros
    
    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        self.__taxa_juros = taxa_juros
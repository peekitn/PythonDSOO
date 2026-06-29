class CategoriaHardware:
    def __init__(self, descricao: str, taxa_logistica: float):
        self.__descricao = descricao
        self.__taxa_logistica = taxa_logistica

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def taxa_logistica(self):
        return self.__taxa_logistica
    
    @taxa_logistica.setter
    def taxa_logistica(self, taxa_logistica):
        self.__taxa_logistica = taxa_logistica
class CategoriaVeiculo:
    def __init__(self, descricao: str, taxa_seguro_fixa: float):
        self.__descricao = descricao
        self.__taxa_seguro_fixa = taxa_seguro_fixa

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def taxa_seguro_fixa(self):
        return self.__taxa_seguro_fixa
    
    @taxa_seguro_fixa.setter
    def taxa_seguro_fixa(self, taxa_seguro_fixa):
        self.__taxa_seguro_fixa = taxa_seguro_fixa
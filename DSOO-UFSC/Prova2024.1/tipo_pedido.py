class TipoPedido:
    def __init__(self, descricao: str, fator_distancia: float):
        self._descricao = descricao
        self._fator_distancia = fator_distancia

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def fator_distancia(self):
        return self._fator_distancia
    
    @fator_distancia.setter
    def fator_distancia(self, fator_distancia):
        self._fator_distancia = fator_distancia
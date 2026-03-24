class ItemPedido:
    def __init__(self, codigo: int, descricao: str, preco_unitario: float):
        self._codigo = codigo
        self._descricao = descricao
        self._preco_unitario = preco_unitario

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
    
    @property
    def preco_unitario(self):
        return self._preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self._preco_unitario = preco_unitario
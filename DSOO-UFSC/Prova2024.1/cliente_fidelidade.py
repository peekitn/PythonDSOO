from cliente import Cliente

class ClienteFidelidade(Cliente):
    def __init__(self, codigo_fidelidade: int, desconto: float, cpf: str, nome: str, endereco: str, telefone: str):
        super().__init__(cpf, nome, endereco, telefone)
        self._codigo_fidelidade = codigo_fidelidade
        self._desconto = desconto

    @property
    def codigo_fidelidade(self):
        return self._codigo_fidelidade
    
    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade):
        self._codigo_fidelidade = codigo_fidelidade

    @property
    def desconto(self):
        return self._desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self._desconto = desconto
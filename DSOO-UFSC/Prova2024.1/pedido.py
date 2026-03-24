from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade

class Pedido:
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self._numero = numero
        self._cliente = cliente
        self._tipo = tipo
        self._itens = []

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def tipo(self):
        return self._tipo

    @property
    def itens(self):
        return self._itens

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def inclui_item_pedido(self, codigo, descricao, preco):
        if codigo is None or descricao is None or preco is None:
            return None
            
        for item in self._itens:
            if item.codigo == codigo:
                return None  # Evita itens duplicados
                
        novo_item = ItemPedido(codigo, descricao, preco)
        self._itens.append(novo_item)
        return novo_item

    def exclui_item_pedido(self, codigo):
        for item in self._itens:
            if item.codigo == codigo:
                self._itens.remove(item)
                return item
        return None

    def calcula_valor_pedido(self, distancia: float):
        # Soma o preço de todos os itens
        valor_itens = sum(item.preco_unitario for item in self._itens)
        
        # Calcula o acréscimo da distância
        acrescimo_distancia = self._tipo.fator_distancia * distancia
        
        # Valor total bruto
        valor_total = valor_itens + acrescimo_distancia
        
        # Aplica desconto se for ClienteFidelidade
        if isinstance(self._cliente, ClienteFidelidade):
            desconto = valor_total * self._cliente.desconto
            valor_total -= desconto
            
        return valor_total
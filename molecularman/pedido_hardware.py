from cliente import Cliente
from categoria_hardware import CategoriaHardware
from componente import Componente
from cliente_atacadista import ClienteAtacadista

class PedidoHardware:
    def __init__(self, codigo: int, cliente: Cliente, categoria: CategoriaHardware):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__categoria = categoria
        self.__componentes = []
        # Inicializar a lista de componentes vazia aqui

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def componentes(self):
        return self.__componentes
    
    @componentes.setter
    def componentes(self, componentes):
        self.__componentes = componentes
    # Getters e Setters para codigo, cliente, categoria
    # Getter para componentes

    '''
    Inclui um novo componente na lista. Retorna o componente se sucesso, None se o codigo ja existir.
    '''
    def incluir_componente(self, codigo: int, descricao: str, preco_base: float):
        if codigo is None or descricao is None or preco_base is None:
            return None
        
        for componente in self.__componentes:
            if componente.codigo == codigo:
                return None
            
        novo_componente = Componente(codigo, descricao, preco_base)
        self.__componentes.append(novo_componente)
        return novo_componente

    '''
    Exclui o componente pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_componente(self, codigo: int):
        if codigo is None:
            return None
        
        for componente in self.__componentes:
            if componente.codigo == codigo:
                self.__componentes.remove(componente)
                return componente
        return None

    '''
    Soma o preco_base de TODOS os componentes presentes no pedido.
    Soma a taxa_logistica da categoria a esse subtotal.
    Se o cliente for ClienteAtacadista, calcula o desconto multiplicando o percentual_desconto 
    pelo valor total atual, e subtrai esse desconto do valor final.
    Retorna float.
    '''
    def calcular_valor_pedido(self):
        total = sum(componente.preco_base for componente in self.__componentes)
        total_com_logistica = total + self.__categoria.taxa_logistica
        if isinstance(self.__cliente, ClienteAtacadista):
            desconto = total_com_logistica * self.__cliente.percentual_desconto
            total_com_logistica -= desconto

        return float(total_com_logistica)
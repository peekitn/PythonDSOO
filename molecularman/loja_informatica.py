from pedido_duplicado_exception import PedidoDuplicadoException
from pedido_hardware import PedidoHardware

class LojaInformatica:
    def __init__(self):
        self.__pedidos = []
        # Inicializar a lista de pedidos vazia aqui
    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos
    # Getter e Setter para pedidos

    '''
    Busca pedido pelo codigo. Retorna None se não encontrar.
    '''
    def busca_pedido_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                return pedido
            return None

    '''
    Adiciona o pedido. Levanta PedidoDuplicadoException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_pedido(self, pedido: PedidoHardware):
        if pedido is None or not isinstance(pedido, PedidoHardware):
            return
        
        if self.busca_pedido_por_codigo(pedido.codigo) is not None:
            raise PedidoDuplicadoException()
        
        self.__pedidos.append(pedido)

    '''
    Remove pelo codigo e retorna o pedido. Retorna None se nao achar.
    '''
    def excluir_pedido(self, codigo: int):
        if codigo is None:
            return None
        
        pedido = self.busca_pedido_por_codigo(codigo)
        if pedido is None:
            return None
        
        self.__pedidos.remove(pedido)
        return pedido

    '''
    Soma o valor total de TODOS os pedidos realizados pelo cliente com o cpf passado por parametro.
    Retorna float.
    '''
    def calcular_faturamento_por_cpf(self, cpf: str):
        if cpf is None:
            return 0.0
        
        faturamento_total = 0.0
        for pedido in self.__pedidos:
            # Acessar o cpf do cliente dentro do pedido e checar se igual ao cpf procurado
            if pedido.cliente.cpf == cpf:
                faturamento_total += pedido.calcular_valor_pedido()
                
        return float(faturamento_total)
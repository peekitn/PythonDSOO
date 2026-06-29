from cliente import Cliente
from categoria_veiculo import CategoriaVeiculo
from servico_extra import ServicoExtra
from cliente_corporativo import ClienteCorporativo

class Locacao:
    def __init__(self, codigo: int, cliente: Cliente, categoria: CategoriaVeiculo):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__categoria = categoria
        self.__servicos_extras = []
        # Inicializar a lista de servicos_extras vazia aqui
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
    def servicos_extras(self):
        return self.__servicos_extras
    
    @servicos_extras.setter
    def servicos_extras(self, servicos_extra):
        self.__servicos_extras = servicos_extra
    # Getters e Setters para codigo, cliente, categoria
    # Getter e Setter para servicos_extras

    '''
    Inclui um novo servico extra na lista. Retorna o servico se sucesso, None se o codigo ja existir.
    '''
    def incluir_servico_extra(self, codigo: int, descricao: str, preco: float):
        if codigo is None or descricao is None or preco is None:
            return None
        
        for servico_extra in self.__servicos_extras:
            if servico_extra.codigo == codigo:
                return None
            
        novo_servico_extra = ServicoExtra(codigo, descricao, preco)
        self.__servicos_extras.append(novo_servico_extra)
        return novo_servico_extra

    '''
    Exclui o servico extra pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_servico_extra(self, codigo: int):
        if codigo is None:
            return None
        
        for servico_extra in self.__servicos_extras:
            if servico_extra.codigo == codigo:
                self.__servicos_extras.remove(servico_extra)
                return servico_extra
        return None

    '''
    Soma o preco de TODOS os servicos extras presentes na locacao.
    Soma a taxa_seguro_fixa da categoria a esse subtotal.
    Se o cliente for ClienteCorporativo, calcula o desconto multiplicando o percentual_desconto 
    pelo valor total atual, e subtrai esse desconto do valor final.
    Retorna float.
    '''
    def calcular_valor_locacao(self):
        total_servicos = sum(servico.preco for servico in self.__servicos_extras)
        
        # Usando as variaveis de instancia (self) corretas
        total_seguro = total_servicos + self.__categoria.taxa_seguro_fixa

        # Validando heranca usando self.__cliente
        if isinstance(self.__cliente, ClienteCorporativo):
            total_seguro -= (total_seguro * self.__cliente.percentual_desconto)

        return float(total_seguro)
from cliente import Cliente
from modalidade_credito import ModalidadeCredito
from parcela import Parcela
from cliente_investidor import ClienteInvestidor

class Emprestimo:
    def __init__(self, codigo: int, cliente: Cliente, modalidade: ModalidadeCredito):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__modalidade = modalidade
        self.__parcelas = []
        # Inicializar a lista de parcelas vazia aqui

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
    def modalidade(self):
        return self.__modalidade
    
    @modalidade.setter
    def modalidade(self, modalidade):
        self.__modalidade = modalidade

    @property
    def parcelas(self):
        return self.__parcelas
    
    @parcelas.setter
    def parcelas(self, parcelas):
        self.__parcelas = parcelas
    # Getters e Setters para codigo, cliente e modalidade
    # Getter para parcelas

    '''
    Inclui uma nova parcela na lista. Retorna a parcela se sucesso, None se o codigo ja existir.
    '''
    def incluir_parcela(self, codigo: int, valor_principal: float, valor_juros: float):
        if codigo is None or valor_principal is None or valor_juros is None:
            return None
        
        for parcela in self.__parcelas:
            if parcela.codigo == codigo:
                return None
            
        nova_parcela = Parcela(codigo, valor_principal, valor_juros)
        self.__parcelas.append(nova_parcela)
        return nova_parcela

    '''
    Exclui a parcela pelo codigo e a retorna. Retorna None se nao achar.
    '''
    def excluir_parcela(self, codigo: int):
        if codigo is None:
            return None
        
        for parcela in self.__parcelas:
            if parcela.codigo == codigo:
                self.__parcelas.remove(parcela)
                return parcela
        return None

    '''
    Soma o valor_principal de TODAS as parcelas.
    Soma o valor_juros de TODAS as parcelas e multiplica pela taxa_juros da modalidade.
    Soma o total principal com o total de juros ajustado.
    Se o cliente for ClienteInvestidor, calcula o cashback multiplicando o percentual_cashback 
    apenas pelo valor total dos juros ajustados, e subtrai isso do montante final.
    Retorna float.
    '''
    def calcular_total_pago(self):
        # Somando extraindo os atributos especificos das parcelas
        soma_principal = sum(parcela.valor_principal for parcela in self.__parcelas)
        soma_juros = sum(parcela.valor_juros for parcela in self.__parcelas)
        
        # Ajustando juros pela modalidade do emprestimo
        juros_ajustado = soma_juros * self.__modalidade.taxa_juros
        total = soma_principal + juros_ajustado

        # Checando heranca e aplicando matemática de desconto
        if isinstance(self.__cliente, ClienteInvestidor):
            desconto = juros_ajustado * self.__cliente.percentual_cashback
            total -= desconto
            
        return float(total)
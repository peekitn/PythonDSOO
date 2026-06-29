from emprestimo_duplicado_exception import EmprestimoDuplicadoException
from emprestimo import Emprestimo

class InstituicaoFinanceira:
    def __init__(self):
        self.__emprestimos = []
        # Inicializar a lista de emprestimos vazia aqui
    @property
    def emprestimos(self):
        return self.__emprestimos
    
    @emprestimos.setter
    def emprestimos(self, emprestimos):
        self.__emprestimos = emprestimos
    # Getter e Setter para emprestimos

    '''
    Busca emprestimo pelo codigo. Retorna None se não encontrar.
    '''
    def busca_emprestimo_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for emprestimo in self.__emprestimos:
            if emprestimo.codigo == codigo:
                return emprestimo
        return None

    '''
    Adiciona o emprestimo. Levanta EmprestimoDuplicadoException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_emprestimo(self, emprestimo: Emprestimo):
        if emprestimo is None or not isinstance(emprestimo, Emprestimo):
            return
        
        if self.busca_emprestimo_por_codigo(emprestimo.codigo) is not None:
            raise EmprestimoDuplicadoException()
        
        self.emprestimos.append(emprestimo)

    '''
    Remove pelo codigo e retorna o emprestimo. Retorna None se nao achar.
    '''
    def excluir_emprestimo(self, codigo: int):
        if codigo is None:
            return None
        
        pedido_excluido = self.busca_emprestimo_por_codigo(codigo)
        if pedido_excluido is None:
            return None
        
        self.__emprestimos.remove(pedido_excluido)
        return pedido_excluido

    '''
    Soma o total pago de TODOS os emprestimos registrados na instituicao.
    Retorna float.
    '''
    def calcular_arrecadacao_total(self):
        total_arrecadado = sum(emprestimo.calcular_total_pago() for emprestimo in self.__emprestimos)
        return float(total_arrecadado)
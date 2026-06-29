from projeto_duplicado_exception import ProjetoDuplicadoException
from projeto import Projeto

class ControladorProjetos:
    def __init__(self):
        self.__projetos = []
        # Inicializar a lista de projetos vazia aqui
    @property
    def projetos(self):
        return self.__projetos
    
    @projetos.setter
    def projetos(self, projetos):
        self.__projetos = projetos
    # Getter e Setter para projetos

    '''
    Busca projeto pelo codigo. Retorna None se não encontrar.
    '''
    def busca_projeto_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for projeto in self.__projetos:
            if projeto.codigo == codigo:
                return projeto
        return None

    '''
    Adiciona o projeto. Levanta ProjetoDuplicadoException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_projeto(self, projeto: Projeto):
        if projeto is None or not isinstance(projeto, Projeto):
            return
        
        if self.busca_projeto_por_codigo(projeto.codigo) is not None:
            raise ProjetoDuplicadoException()
    
        self.__projetos.append(projeto)
    '''
    Remove pelo codigo e retorna o projeto. Retorna None se nao achar.
    '''
    def excluir_projeto(self, codigo: int):
        if codigo is None:
            return None
        
        projeto_excluir = self.busca_projeto_por_codigo(codigo)
        if projeto_excluir is not None:
            self.__projetos.remove(projeto_excluir)
            return projeto_excluir
        
        return None


    '''
    Soma o custo total de TODOS os projetos que pertencem ao cpf passado como parametro.
    Retorna float.
    '''
    def calcular_custo_total_por_cpf(self, cpf: str):
        total = 0.0
        for projeto in self.__projetos:
            if projeto.desenvolvedor.cpf == cpf:
                total += projeto.calcular_custo_projeto()
        return float(total)
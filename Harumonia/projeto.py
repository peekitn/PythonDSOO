from desenvolvedor import Desenvolvedor
from criticidade_projeto import CriticidadeProjeto
from registro_trabalho import RegistroTrabalho
from desenvolvedor_senior import DesenvolvedorSenior

class Projeto:
    def __init__(self, codigo: int, desenvolvedor: Desenvolvedor, criticidade: CriticidadeProjeto):
        self.__codigo = codigo
        self.__desenvolvedor = desenvolvedor
        self.__criticidade = criticidade
        self.__registros = []
        # Inicializar a lista de registros vazia aqui
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def desenvolvedor(self):
        return self.__desenvolvedor
    
    @desenvolvedor.setter
    def desenvolvedor(self, desenvolvedor):
        self.__desenvolvedor = desenvolvedor

    @property
    def criticidade(self):
        return self.__criticidade
    
    @criticidade.setter
    def criticidade(self, criticidade):
        self.__criticidade = criticidade

    @property
    def registros(self):
        return self.__registros
    
    @registros.setter
    def registros(self, registros):
        self.__registros = registros
    # Getters e Setters para codigo, desenvolvedor, criticidade
    # Getter para registros

    '''
    Inclui um novo registro na lista. Retorna o registro se sucesso, None se o codigo ja existir.
    '''
    def incluir_registro_trabalho(self, codigo: int, horas_trabalhadas: int, indice_stress: float):
        if codigo is None or horas_trabalhadas is None or indice_stress is None:
            return None
        
        for registro in self.__registros:
            if registro.codigo == codigo:
                return None
            
        novo_registro = RegistroTrabalho(codigo, horas_trabalhadas, indice_stress)
        self.__registros.append(novo_registro)
        return novo_registro

    '''
    Exclui o registro pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_registro_trabalho(self, codigo: int):
        if codigo is None:
            return None
        
        for registro in self.__registros:
            if registro.codigo == registro:
                self.__registros.remove(registro)
                return registro
        return None

    '''
    Calcula a media do indice_stress de todos os registros daquele projeto.
    Se a lista de registros estiver vazia, deve retornar 0.0.
    Retorna float.
    '''
    def calcular_media_stress(self):
        if len(self.__registros) == 0:
            return 0.0
            
        soma_stress = sum(registro.indice_stress for registro in self.__registros)
        media = soma_stress / len(self.__registros)
        return float(media)

    '''
    Soma as horas_trabalhadas de TODOS os registros.
    Multiplica o total de horas pelo valor_hora do desenvolvedor.
    Multiplica esse resultado pelo fator_urgencia da criticidade do projeto.
    Se o desenvolvedor for DesenvolvedorSenior, soma o bonus_lideranca ao final.
    Retorna float.
    '''
    def calcular_custo_projeto(self):
        total_horas = sum(registro.horas_trabalhadas for registro in self.__registros)
        custo_base = total_horas * self.__desenvolvedor.valor_hora
        custo_com_urgencia = custo_base * self.__criticidade.fator_urgencia

        if isinstance(self.__desenvolvedor, DesenvolvedorSenior):
            custo_com_urgencia += self.__desenvolvedor.bonus_lideranca

        return float(custo_com_urgencia)
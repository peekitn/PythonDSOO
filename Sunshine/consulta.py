from paciente import Paciente
from medico import Medico
from exame import Exame
from paciente_plano_saude import PacientePlanoSaude

class Consulta:
    def __init__(self, codigo: int, paciente: Paciente, medico: Medico):
        self.__codigo = codigo
        self.__paciente = paciente
        self.__medico = medico
        self.__exames = []
        # Inicializar a lista de exames vazia aqui
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def paciente(self):
        return self.__paciente
    
    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def medico(self):
        return self.__medico
    
    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    @property
    def exames(self):
        return self.__exames
    
    @exames.setter
    def exames(self, exames):
        self.__exames = exames
    # Getters e Setters para codigo, paciente, medico
    # Getter para exames

    '''
    Inclui um novo exame na lista. Retorna o exame se sucesso, None se o codigo ja existir.
    '''
    def incluir_exame(self, codigo: int, descricao: str, custo: float):
        if codigo is None or descricao is None or custo is None:
            return None
        
        for exame in self.__exames:
            if exame.codigo == codigo:
                return None
        
        novo_exame = Exame(codigo, descricao, custo)
        self.__exames.append(novo_exame)
        return novo_exame
    '''
    Exclui o exame pelo codigo e o retorna. Retorna None se nao achar.
    '''
    def excluir_exame(self, codigo: int):
        if codigo is None:
            return None
        
        for exame in self.__exames:
            if exame.codigo == codigo:
                self.__exames.remove(exame)
                return exame
        return None

    '''
    Soma o valor_consulta do medico com o custo de TODOS os exames.
    Se o paciente for PacientePlanoSaude, aplica o percentual_desconto sobre o total.
    Exemplo: Se o total for 1000 e o desconto 0.20, o valor final é 800.
    Retorna float.
    '''
    def calcular_valor_total(self):
        total_exames = sum(exame.custo for exame in self.__exames)
        valor_base = self.__medico.valor_consulta + total_exames

        # Verificando heranca no objeto self.__paciente e aplicando matematica
        if isinstance(self.__paciente, PacientePlanoSaude):
            desconto = valor_base * self.__paciente.percentual_desconto
            valor_base -= desconto

        return float(valor_base)
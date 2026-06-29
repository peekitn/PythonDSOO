from consulta_duplicada_exception import ConsultaDuplicadaException
from consulta import Consulta

class Clinica:
    def __init__(self):
        self.__consultas = []
        # Inicializar a lista de consultas vazia aqui
    @property
    def consultas(self):
        return self.__consultas
    
    @consultas.setter
    def consultas(self, consultas):
        self.__consultas = consultas
    # Getter e Setter para consultas

    '''
    Busca consulta pelo codigo. Retorna None se não encontrar.
    '''
    def busca_consulta_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        
        for consulta in self.__consultas:
            if consulta.codigo == codigo:
                return consulta
        return None

    '''
    Adiciona a consulta. Levanta ConsultaDuplicadaException se o codigo ja existir.
    Tratar tambem instâncias incorretas ou None.
    '''
    def incluir_consulta(self, consulta: Consulta):
        if consulta is None or not isinstance(consulta, Consulta):
            return
        
        if self.busca_consulta_por_codigo(consulta.codigo) is not None:
            raise ConsultaDuplicadaException()
    
        self.consultas.append(consulta)

    '''
    Remove pelo codigo e retorna a consulta. Retorna None se nao achar.
    '''
    def excluir_consulta(self, codigo: int):
        if codigo is None:
            return None
        
        exclusao_consulta = self.busca_consulta_por_codigo(codigo)

        if exclusao_consulta is None:
            return None
        
        self.__consultas.remove(exclusao_consulta)
        return exclusao_consulta

    '''
    Soma o valor total de TODAS as consultas que foram realizadas pelo medico 
    com o CRM passado como parametro.
    Retorna float.
    '''
    def calcular_faturamento_por_medico(self, crm: str):
        if crm is None:
            return 0.0
        
        faturamento_total = 0.0
        for consulta in self.__consultas:
            # Verifica se o crm do medico da consulta bate com o procurado
            if consulta.medico.crm == crm:
                faturamento_total += consulta.calcular_valor_total()
                
        return float(faturamento_total)
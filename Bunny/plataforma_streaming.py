from serie_duplicada_exception import SerieDuplicadaException
from serie import Serie

class PlataformaStreaming:
    def __init__(self):
        self.__series = []
        # Inicializar a lista de series vazia

    # Implementar getter e setter para series
    @property
    def series(self):
        return self.__series
    
    @series.setter
    def series(self, series):
        self.__series = series

    '''
    Busca serie pelo codigo.
    Se a serie nao existir ou o codigo for invalido, deve retornar None.
    Caso contrario, retorna a serie.
    '''
    def busca_serie_por_codigo(self, codigo: int):
        if codigo is None:
            return None
        for serie in self.__series:
            if serie.codigo == codigo:
                return serie
        return None

    '''
    Incluir serie na lista.
    Tratar os casos de instancias incorretas (None ou tipo errado).
    Caso a serie já exista na lista (mesmo codigo), gerar a excecao: 
    SerieDuplicadaException
    '''
    def incluir_serie(self, serie: Serie):
        if not isinstance(serie, Serie):
            return
        if self.busca_serie_por_codigo(serie.codigo) is not None:
            raise SerieDuplicadaException()
        self.__series.append(serie)

    '''
    Exclui serie pelo codigo.
    Se a serie nao existir, deve retornar None.
    Caso contrario, retorna a serie excluida.
    '''
    def excluir_serie(self, codigo: int):
        if codigo is None:
            return None
        serie = self.busca_serie_por_codigo(codigo)
        if serie is None:
            return None
        self.__series.remove(serie)
        return serie

    '''
    Percorre a lista de series e retorna uma nova lista contendo apenas
    as series que possuem uma nota_critica maior ou igual ao parametro fornecido.
    '''
    def recomendar_series_alta_nota(self, nota_minima: float):
        series_recomendadas = []
        for serie in self.__series:
            if serie.nota_critica >= nota_minima:
                series_recomendadas.append(serie)
        return series_recomendadas
from episodio import Episodio

class Serie:
    def __init__(self, codigo: int, titulo: str, nota_critica: float):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__nota_critica = nota_critica
        self.__episodios = []
        # O atributo de episodios deve ser inicializado como uma lista vazia
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def nota_critica(self):
        return self.__nota_critica
    
    @nota_critica.setter
    def nota_critica(self, nota_critica):
        self.__nota_critica = nota_critica

    @property
    def episodios(self):
        return self.__episodios
    
    @episodios.setter
    def episodios(self, episodios):
        self.__episodios = episodios
    # Implementar getters e setters para codigo, titulo e nota_critica
    # Implementar getter para a lista de episodios

    '''
    Inclui um novo episodio na lista de episodios da serie.
    Nao deve ser possivel incluir episodios duplicados (com o mesmo numero).
    Retornar o episodio incluido em caso de sucesso e None em caso de duplicidade.
    '''
    def incluir_episodio(self, numero: int, titulo: str, duracao_minutos: int):
        if numero is None or titulo is None or duracao_minutos is None:
            return None
        for episodio in self.__episodios:
            if episodio.numero == numero:
                return None
        novo_episodio = Episodio(numero, titulo, duracao_minutos)
        self.__episodios.append(novo_episodio)
        return novo_episodio

    '''
    Exclui um episodio da serie pelo numero e retorna o episodio excluido.
    Caso o episodio nao exista, retorne None.
    '''
    def excluir_episodio(self, numero: int):
        if numero is None:
            return None
        for episodio in self.__episodios:
            if episodio.numero == numero:
                self.__episodios.remove(episodio)
                return episodio
        return None

    '''
    Soma a duracao_minutos de todos os episodios presentes na lista da série.
    @return um int correspondente aos minutos totais da serie.
    '''
    def calcular_duracao_total(self):
        total = sum(episodio.duracao_minutos for episodio in self.__episodios)
        return total
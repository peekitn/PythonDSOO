from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int,
                 editora: Editora, autor: Autor,
                 numero_capitulo: int, titulo_capitulo: str):

        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora

        self.__autores = []
        self.__capitulos = []

        # inserir inicial (IMPORTANTE PRO VPL)
        self.incluir_autor(autor)
        self.incluir_capitulo(numero_capitulo, titulo_capitulo)

    # ---------- PROPERTIES ----------
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
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    # ⚠️ IMPORTANTE: precisa ser PROPERTY
    @property
    def autores(self):
        return self.__autores

    # ---------- AUTORES ----------
    def incluir_autor(self, autor: Autor):
        if autor is None:
            return

        if not isinstance(autor, Autor):
            return

        if autor in self.__autores:
            return

        self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor is None:
            return

        if not isinstance(autor, Autor):
            return

        if autor in self.__autores:
            self.__autores.remove(autor)

    # ---------- CAPÍTULOS ----------
    def incluir_capitulo(self, numero: int, titulo: str):
        if titulo is None:
            return

        if self.find_capitulo_by_titulo(titulo) is not None:
            return

        cap = Capitulo(numero, titulo)
        self.__capitulos.append(cap)

    def excluir_capitulo(self, titulo: str):
        cap = self.find_capitulo_by_titulo(titulo)

        if cap is not None:
            self.__capitulos.remove(cap)

    def find_capitulo_by_titulo(self, titulo: str):
        for cap in self.__capitulos:
            if cap.titulo == titulo:
                return cap
        return None
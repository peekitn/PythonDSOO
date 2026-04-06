from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if livro is None:
            return

        if not isinstance(livro, Livro):
            return

        if livro in self.__livros:
            return

        self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if livro is None:
            return

        if not isinstance(livro, Livro):
            return

        if livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
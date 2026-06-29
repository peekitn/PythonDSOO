from artista import Artista
from musica import Musica
from genero import Genero

class Album:
    def __init__(self, codigo: int, titulo: str, ano: int, genero: Genero, 
                 artista_inicial: Artista, faixa_inicial: int, titulo_musica_inicial: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__genero = genero
        self.__artistas = []
        self.__musicas = []


        self.incluir_artista(artista_inicial)
        self.incluir_musica(faixa_inicial, titulo_musica_inicial)

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
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        if isinstance(genero, Genero):
            self.__genero = genero 

    def incluir_artista(self, artista: Artista):
        if artista is None:
            return
        if not isinstance(artista, Artista):
            return
        if artista not in self.__artistas:
            self.__artistas.append(artista)
    
    def excluir_artista(self, artista: Artista):
        if artista is None:
            return
        if not isinstance(artista, Artista):
            return
        if artista in self.__artistas:
            self.__artistas.remove(artista)

    def find_musica_by_titulo(self, titulo: str):
        for musica in self.__musicas:
            if musica.titulo == titulo:
                return musica
        return None 

    def incluir_musica(self, faixa: int, titulo: str):
        if titulo is None:
            return

        if self.find_musica_by_titulo(titulo) is not None:
            return
        
        nova_musica = Musica(faixa, titulo)
        self.__musicas.append(nova_musica)

    def excluir_musica(self, titulo: str):
        musica = self.find_musica_by_titulo(titulo)
        if musica is not None:
            self.__musicas.remove(musica)
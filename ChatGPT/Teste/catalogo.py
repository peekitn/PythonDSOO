from album import Album

class Catalogo:
    def __init__(self):
        self.__albuns = []

    def incluir_album(self, album: Album):
        if album is None:
            return
        if not isinstance(album, Album):
            return
        if album not in self.__albuns:
            self.__albuns.append(album)

    def excluir_album(self, album: Album):
        if album is None:
            return
        if not isinstance(album, Album):
            return
        if album in self.__albuns:
            self.__albuns.remove(album)

    @property
    def albuns(self):
        return self.__albuns
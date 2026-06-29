from aluno import Aluno
from professor import Professor

class Curso:
    def __init__(self, codigo: int, nome: str, professor: Professor, 
                 matricula_inicial: int, nome_aluno_inicial: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__professor = professor
        
        self.__alunos = []

        self.adicionar_aluno(matricula_inicial, nome_aluno_inicial)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        if isinstance(professor, Professor):
            self.__professor = professor

    @property
    def alunos(self):
        return self.__alunos

    def buscar_aluno(self, matricula: int):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def adicionar_aluno(self, matricula: int, nome: str):
        if nome is None:
            return
        if self.buscar_aluno(matricula) is not None:
            return 
            
        novo_aluno = Aluno(matricula, nome)
        self.__alunos.append(novo_aluno)

    def atualizar_aluno(self, matricula: int, novo_nome: str):
        if novo_nome is None:
            return
            
        aluno_encontrado = self.buscar_aluno(matricula)
        
        if aluno_encontrado is not None:
            aluno_encontrado.nome = novo_nome

    def remover_aluno(self, matricula: int):

        aluno_encontrado = self.buscar_aluno(matricula)
        
        if aluno_encontrado is not None:
            self.__alunos.remove(aluno_encontrado) 
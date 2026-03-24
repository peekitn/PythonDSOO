class Aluno():
    def __init__(self, nome: str, endereco: str, telefone: int, idade: int, matricula: int):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self.idade = idade
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Idade deve ser um número inteiro")
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor
    
    @property
    def matricula(self):
        return self._matricula
    
    def mostra_dados(self):
        print(f"Nome = {self._nome}\nEndereco = {self._endereco}\nTelefone = {self._telefone}\nIdade = {self._idade}\nMatricula = {self._matricula}\n")
        
    def faz_aniversario(self):
        self._idade += 1

aluno1 = Aluno("Anderson", "Rua A", 123456, 19, 1001)
aluno2 = Aluno("Maria", "Rua B", 987654, 21, 1002)
aluno3 = Aluno("Joao", "Rua C", 555555, 18, 1003)

aluno1.mostra_dados()
aluno2.mostra_dados()
aluno3.mostra_dados()

aluno1.faz_aniversario()
aluno2.faz_aniversario()
aluno3.faz_aniversario()

print("Depois do aniversario:")
aluno1.mostra_dados()
aluno2.mostra_dados()
aluno3.mostra_dados()
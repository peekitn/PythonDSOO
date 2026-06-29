from usuario import Usuario
from modelo_ai import ModeloAI
from requisicao import Requisicao
from usuario_pro import UsuarioPro

class SessaoGeracao:
    def __init__(self, codigo: int, usuario: Usuario, modelo: ModeloAI):
        self.__codigo = codigo
        self.__usuario = usuario
        self.__modelo = modelo
        self.__requisicoes = []
        # Inicializar a lista de requisicoes vazia aqui
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def requisicoes(self):
        return self.__requisicoes
    
    @requisicoes.setter
    def requisicoes(self, requisicoes):
        self.__requisicoes = requisicoes
    # Getters e Setters para codigo, usuario e modelo
    # Getter para requisicoes

    '''
    Inclui uma nova requisicao na lista. Retorna a requisicao se sucesso, None se o codigo ja existir.
    '''
    def incluir_requisicao(self, codigo: int, prompt: str, custo_base: float):
        if codigo is None or prompt is None or custo_base is None:
            return None
        
        for requisicao in self.__requisicoes:
            if requisicao.codigo == codigo:
                return None
            
        nova_requisicao = Requisicao(codigo, prompt, custo_base)
        self.__requisicoes.append(nova_requisicao)
        return nova_requisicao

    '''
    Exclui a requisicao pelo codigo e a retorna. Retorna None se nao achar.
    '''
    def excluir_requisicao(self, codigo: int):
        if codigo is None:
            return None
        
        for requisicao in self.__requisicoes:
            if requisicao.codigo == codigo:
                self.__requisicoes.remove(requisicao)
                return requisicao
        return None

    '''
    Soma o custo_base de TODAS as requisicoes presentes na sessao.
    Multiplica esse total pelo fator_computacional do modelo escolhido.
    Se o usuario for UsuarioPro, calcula o desconto multiplicando o desconto_percentual 
    pelo valor recem calculado, e subtrai esse desconto do valor final.
    Retorna float.
    '''
    def calcular_custo_total(self):
        total = sum(requisicao.custo_base for requisicao in self.__requisicoes)
        multiplica = total * self.__modelo.fator_computacional

        if isinstance(self.__usuario, UsuarioPro):
            multiplica -= (multiplica * self.__usuario.desconto_percentual) 

        return float(multiplica)
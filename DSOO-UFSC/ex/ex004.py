"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def ordena(self, array_para_ordenar:[]):
        """Realiza a ordenacao do conteudo do array recebido como parâmetro"""
        n = len(array_para_ordenar)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if array_para_ordenar[j] > array_para_ordenar[j + 1]:
                    temp = array_para_ordenar[j]
                    array_para_ordenar[j] = array_para_ordenar[j + 1]
                    array_para_ordenar[j + 1] = temp
        return array_para_ordenar

    def to_string(self, array_ordenado:[]):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        resultado = ""
        
        for i in range(len(array_ordenado)):
            resultado +=str(array_ordenado[i])
            if i != len(array_ordenado) - 1:
                resultado += ","
        return resultado
        
ordenador = Ordenacao()

entrada = [4, 3, 2, 1, 5]
ordenado = ordenador.ordena(entrada)
saida = ordenador.to_string(ordenado)

print(saida)
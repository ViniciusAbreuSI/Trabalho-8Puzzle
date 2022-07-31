class Result:
    """
    Classe que escreve o resultado da busca
    """
    def __init__(self, nameMethod, timeMethod, path, visitedNodes):
        """
        Metodo construtor da classe __init__
        """
        self.name = nameMethod
        self.time = timeMethod
        self.path = path
        self.visitedNodes = visitedNodes

    def __repr__(self):
        """
        Sobrescrita do metodo "__repr__" apresenta a classe como uma string
        """
        result_string = f'Metodo: {self.name}\n'
        result_string += f'Tempo: {round(self.time, 6)} segundos\n'
        result_string += f'Quantidade de nos visitados: {len(self.visitedNodes) - 1 if self.name == "Busca bidirecional" else len(self.visitedNodes)}\n'
        result_string += f'Quantidade de jogadas: {len(self.path)}\n'
        result_string += f'Caminho das jogadas\n'

        for i in range(len(self.path)):
            result_string += f'Jogada {i + 1}\n' + str(self.path[i])

            if i < len(self.path) - 1:
                result_string += '\n'

        return result_string

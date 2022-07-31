class Node:
    """
    Classe que representa o no.
    """

    def __init__(self, state, goal, parent=None):
        """
        Metodo construtor da classe Node.
        """
        self.state = state
        self.neighbors = []
        self.visited_right = False
        self.visited_left = False
        self.parent_right = None
        self.parent_left = None
        self.parent = parent
        self.g = 0 if not parent else parent.g + 1
        self.h = self.getH(goal)
        self.f = self.g + self.h

    def __repr__(self):
        """
        Sobrescrita do metodo __repr__ que representa a classe como uma string
        """
        representantion = ''

        for i in range(3):
            for j in range(3):
                representantion += str(self.state[3 * i + j])

                if j == 2 and i != 2:
                    representantion += '\n'
                else:
                    representantion += ' '

        return representantion

    def __eq__(self, another_node):
        """
        Sobrescrita do metodo de igualdade (__eq__).
        """
        return Node.stateAsString(self.state) == Node.stateAsString(another_node.state)

    def getH(self, goal):
        value_of_h = 0

        for index, value in enumerate(goal):
            if self.state[index] != value and value != 0:
                value_of_h += 1

        return value_of_h

    def addNeighbor(self, node):
        """
        Metodo que adiciona um node adjacente.
        """
        self.neighbors.append(node)

    def neighboringStates(self):
        """
        Metodo que retorna os estados dos nos vizinhos. Dessa forma os nos sao criados no momento da execusao do algoritmo, otimizando a busca.
        """
        index = self.state.index(0)

        if index == 0:
            return [self.move(movement) for movement in ['down', 'right']]
        elif index == 1:
            return [self.move(movement) for movement in ['down', 'left', 'right']]
        elif index == 2:
            return [self.move(movement) for movement in ['down', 'left']]
        elif index == 3:
            return [self.move(movement) for movement in ['up', 'down', 'right']]
        elif index == 4:
            return [self.move(movement) for movement in ['up', 'down', 'left', 'right']]
        elif index == 5:
            return [self.move(movement) for movement in ['up', 'down', 'left']]
        elif index == 6:
            return [self.move(movement) for movement in ['up', 'right']]
        elif index == 7:
            return [self.move(movement) for movement in ['up', 'left', 'right']]
        else:
            # index == 8
            return [self.move(movement) for movement in ['up', 'left']]

    def move(self, movement):
        """
        Metodo que retorna o estado apos um movimento.
        """
        index = self.state.index(0)

        new_state = self.state.copy()

        if movement == 'up':
            new_state[index], new_state[index -
                                        3] = new_state[index - 3], new_state[index]
        elif movement == 'down':
            new_state[index], new_state[index +
                                        3] = new_state[index + 3], new_state[index]
        elif movement == 'left':
            new_state[index], new_state[index -
                                        1] = new_state[index - 1], new_state[index]
        else:
            # movement == 'right'
            new_state[index], new_state[index +
                                        1] = new_state[index + 1], new_state[index]

        return new_state

    @staticmethod
    def stateAsString(state):
        """
        Metodo estatico que retorna o estado de um no como uma string.
        """
        new_state = [str(element) for element in state]

        return ''.join(new_state)

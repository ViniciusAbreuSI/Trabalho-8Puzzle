import time
from node import Node
from result import Result

class Controller:
    """
    Classe que representa o grafo
    """

    def __init__(self, initial_state):
        """
        Metodo construtor da classe
        """
        self.initial_state = initial_state
        self.final_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.nodes = {}
        self.addNode(self.initial_state)
        self.addNode(self.final_state)
        self.results = []

    def appendResultArray(self, method_name, method_time, path, visited_nodes):
        """
        Metodo que adiciona um resultado a lista de resultados
        """
        self.results.append(
            Result(method_name, method_time, path, visited_nodes))

    def addNode(self, state):
        """
        Metodo que adiciona um no ao grafo
        """
        stateAsString = Node.stateAsString(state)

        if not self.nodes.get(stateAsString):
            node = Node(state, self.final_state)

            self.nodes[stateAsString] = node

        return self.nodes.get(stateAsString)

    def addEdge(self, state1, state2):
        """
        Metodo que adiciona uma aresta ao no
        """
        state_1_as_string = Node.stateAsString(state1)

        state_2_as_string = Node.stateAsString(state2)

        if not (self.nodes.get(state_1_as_string) and self.nodes.get(state_2_as_string)):
            return False

        node_1 = self.nodes.get(state_1_as_string)

        node_2 = self.nodes.get(state_2_as_string)

        node_1.add_neighbor(node_2)

        node_2.add_neighbor(node_1)

        return True

    def getNode(self, state):
        """
        Metodo que retorna um no do grafo
        """
        return self.nodes.get(Node.stateAsString(state))

    def bidirectionalAuxiliarMethod(self, node):
        """
        Metodo auxiliar da busca bidirecional que verifica se o no e a intersecao da busca
        """
        return node.visited_left and node.visited_right

    def bidirectionalSearch(self):
        """
        Metodo que realiza a busca bidirecional e salva o resultado na lista de resultados
        """
        begin = time.time()

        initial_node = self.getNode(self.initial_state)

        final_node = self.getNode(self.final_state)

        queue = [initial_node, final_node]

        initial_node.visited_right = True

        final_node.visited_left = True

        visited_nodes = []

        while queue:
            node = queue.pop(0)

            if self.bidirectionalAuxiliarMethod(node):
                end = time.time()

                method_time = end - begin

                copy_node = node

                path = []

                while node:
                    path.append(node)

                    node = node.parent_right

                path.reverse()

                del path[-1]

                while copy_node:
                    path.append(copy_node)

                    copy_node = copy_node.parent_left

                self.appendResultArray('Busca bidirecional',
                                method_time, path, visited_nodes)

                return True
            else:
                states = node.neighboringStates()

                neighbors = [self.addNode(state) for state in states]

                for neighbor in neighbors:
                    if node.visited_left and not neighbor.visited_left:
                        neighbor.parent_left = node

                        neighbor.visited_left = True

                        queue.append(neighbor)

                        visited_nodes.append(neighbor)

                    if node.visited_right and not neighbor.visited_right:
                        neighbor.parent_right = node

                        neighbor.visited_right = True

                        queue.append(neighbor)

                        visited_nodes.append(neighbor)

        end = time.time()

        method_time = end - begin

        self.appendResultArray('Busca bidirecional', method_time, [], visited_nodes)

        return False

    def graphReset(self):
        """
        Metodo que reinicializa o grafo
        """
        self.nodes = {}
        self.addNode(self.initial_state)
        self.addNode(self.final_state)

    def starASearch(self):
        """
        Metodo que realiza a busca pelo metodo A-estrela e salva o resultado na lista de resultados
        """
        begin = time.time()

        self.graphReset()

        border = []
        path = []

        visited_nodes = []

        border_size = 0

        initial_node = self.getNode(self.initial_state)

        final_node = self.getNode(self.final_state)

        border.append(initial_node)

        current = border.pop(0)

        while current and not current == final_node:
            neighbors = []

            for state in current.neighboringStates():
                neighbor = Node(state, self.final_state, current)

                neighbors.append(neighbor)

            for neighbor in neighbors:
                if not neighbor in border:
                    border.append(neighbor)

                    visited_nodes.append(neighbor)

            border.sort(key=lambda x: x.f)

            if border_size < len(border):
                border_size = len(border)

            current = border.pop(0)

        while current.parent is not None:
            path.insert(0, current)

            current = current.parent

        end = time.time()

        method_time = end - begin

        self.appendResultArray('A-estrela', method_time, path, visited_nodes)

        return path

from module.Node import Node


class Graph:

    def __init__(self, nodes, weight_matrix, undirected):
        self.nodes = nodes
        self.weight_matrix = weight_matrix
        self.undirected = undirected

    def add_neighbour(self, id1, id2, weight):
        node1 = node2 = None
        for node in self.nodes:
            if node.id == id1:
                node1 = node
            if node.id == id2:
                node2 = node
        if node1 is not None and node2 is not None:
            node1.add_neighbour(node2)
            self.weight_matrix[node1.id][node2.id] = weight
        if self.undirected is True:
            node2.add_neighbour(node1)
            self.weight_matrix[node2.id][node1.id] = weight

    def add_neighbour_simple(self, id1, id2):
        node1 = node2 = None
        for node in self.nodes:
            if node.id == id1:
                node1 = node
            if node.id == id2:
                node2 = node
        if node1 is not None and node2 is not None:
            node1.add_neighbour(node2)

    # Just for Tests
    def clone(self):
        new_nodes = []
        for node in self.nodes:
            new_node = Node(node.id)
            new_nodes.append(new_node)
        cloned = Graph(new_nodes, self.weight_matrix, self.undirected)
        for node in self.nodes:
            if node.neighbour is not None:
                for neigh in node.neighbour:
                    cloned.nodes[node.id].neighbour.append(cloned.nodes[neigh.id])
        return cloned

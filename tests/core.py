import unittest
from module.Graph import Graph
from module.WeightMatrix import WeightMatrix
from module.Node import Node
from module import main


class TestDijkstra(unittest.TestCase):

    def test_basic(self):
        nodes = [0, 1, 2, 3]
        weight_matrix = WeightMatrix(len(nodes))
        weight_matrix = weight_matrix.matrix
        for node in nodes:
            nodes[node] = Node(node)
        graph = Graph(nodes, weight_matrix, True)
        graph.add_neighbour(0, 1, 3)
        self.assertEqual(main.dijkstra(graph, 0, 1), 3)

    def test_basic2(self):
        nodes = [0, 1, 2, 3]
        weight_matrix = WeightMatrix(len(nodes))
        weight_matrix = weight_matrix.matrix
        for node in nodes:
            nodes[node] = Node(node)
        graph = Graph(nodes, weight_matrix, True)
        graph.add_neighbour(0, 1, 3)
        graph.add_neighbour(0, 2, 2)
        graph.add_neighbour(1, 2, 5)
        graph.add_neighbour(2, 3, 1)
        self.assertEqual(main.dijkstra(graph, 3, 0), 3)

    def test_shortest_path(self):
        nodes = [0, 1, 2, 3, 4, 5, 6]
        weight_matrix = WeightMatrix(len(nodes))
        weight_matrix = weight_matrix.matrix
        for node in nodes:
            nodes[node] = Node(node)
        graph = Graph(nodes, weight_matrix, True)
        graph.add_neighbour(0, 1, 1)
        graph.add_neighbour(0, 3, 0)
        graph.add_neighbour(0, 5, 1)
        graph.add_neighbour(1, 4, 6)
        graph.add_neighbour(1, 5, 4)
        graph.add_neighbour(1, 2, 3)
        graph.add_neighbour(4, 6, 1)
        graph.add_neighbour(5, 6, 8)
        self.assertEqual(main.dijkstra(graph, 0, 6), 8)

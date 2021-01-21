import unittest
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
        nodes[0].add_neighbour(nodes[1], 3, weight_matrix, True)
        self.assertEqual(main.dijkstra(nodes, weight_matrix, 0, 1), 3)

    def test_basic2(self):
        nodes = [0, 1, 2, 3]
        weight_matrix = WeightMatrix(len(nodes))
        weight_matrix = weight_matrix.matrix
        for node in nodes:
            nodes[node] = Node(node)
        nodes[0].add_neighbour(nodes[1], 3, weight_matrix, True)
        nodes[0].add_neighbour(nodes[2], 2, weight_matrix, True)
        nodes[1].add_neighbour(nodes[2], 5, weight_matrix, True)
        nodes[2].add_neighbour(nodes[3], 1, weight_matrix, True)
        self.assertEqual(main.dijkstra(nodes, weight_matrix, 0, 3), 3)

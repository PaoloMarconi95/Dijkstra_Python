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
        self.assertEqual(main.dijkstra(nodes, weight_matrix, 3, 0), 3)

    def test_shortest_path(self):
        nodes = [0, 1, 2, 3, 4, 5, 6]
        weight_matrix = WeightMatrix(len(nodes))
        weight_matrix = weight_matrix.matrix
        for node in nodes:
            nodes[node] = Node(node)
        nodes[0].add_neighbour(nodes[1], 1, weight_matrix, True)
        nodes[0].add_neighbour(nodes[3], 0, weight_matrix, True)
        nodes[0].add_neighbour(nodes[5], 1, weight_matrix, True)
        nodes[1].add_neighbour(nodes[4], 6, weight_matrix, True)
        nodes[1].add_neighbour(nodes[5], 4, weight_matrix, True)
        nodes[1].add_neighbour(nodes[2], 3, weight_matrix, True)
        nodes[4].add_neighbour(nodes[6], 1, weight_matrix, True)
        nodes[5].add_neighbour(nodes[6], 8, weight_matrix, True)
        self.assertEqual(main.dijkstra(nodes, weight_matrix, 0, 6), 8)

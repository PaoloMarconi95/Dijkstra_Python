import numpy as np
from Node import Node

number_of_nodes = 6
weight_matrix = np.zeros((number_of_nodes, number_of_nodes))
undirected_graph = True
debug = False


def main():
    nodes = prepare_graph()
    dijkstra(nodes)
    for node in nodes:
        node.print_path()


def prepare_graph():
    nodes = [0, 1, 2, 3, 4, 5]
    for node in nodes:
        nodes[node] = Node(node)
    nodes[0].add_neighbour(nodes[1], 4, weight_matrix, undirected_graph)
    nodes[0].add_neighbour(nodes[2], 3, weight_matrix, undirected_graph)
    nodes[1].add_neighbour(nodes[2], 1, weight_matrix, undirected_graph)
    nodes[1].add_neighbour(nodes[3], 2, weight_matrix, undirected_graph)
    nodes[2].add_neighbour(nodes[3], 4, weight_matrix, undirected_graph)
    nodes[2].add_neighbour(nodes[4], 3, weight_matrix, undirected_graph)
    nodes[3].add_neighbour(nodes[4], 2, weight_matrix, undirected_graph)
    nodes[3].add_neighbour(nodes[5], 1, weight_matrix, undirected_graph)
    nodes[4].add_neighbour(nodes[5], 6, weight_matrix, undirected_graph)
    return nodes


def dijkstra(nodes):
    for node in nodes:
        if debug:
            print("Node " + str(node.id))
        for neighbour in node.neighbour:
            if node.current_value > 0:
                possible = node.current_value + weight_matrix[node.id][neighbour.id]
                if (possible < neighbour.current_value) | (neighbour.current_value == -1):
                    neighbour.current_value = possible
                    if debug:
                        print("Found new minimum of " + str(possible)
                              + " with neighbour " + str(neighbour.id))
            else:
                # we're on 1st node
                neighbour.current_value = weight_matrix[node.id][neighbour.id]
                if debug:
                    print("Found new minimum of " + str(weight_matrix[node.id][neighbour.id]))
        node.completed = True
        node.remove_from_neighbour()
        if debug:
            print("Node " + str(node.id) + " Done. \n\n")


main()

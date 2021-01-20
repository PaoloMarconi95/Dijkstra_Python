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


# Custom preparation of the graph. Future release will allow graphic interface
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
        for current_neighbour in node.neighbour:
            if node.current_value > 0:
                possible = node.current_value + weight_matrix[node.id][current_neighbour.id]
                if (possible < current_neighbour.current_value) | (current_neighbour.current_value == -1):
                    current_neighbour.current_value = possible
                    new_optimus = node.optimus_path
                    new_optimus.append(node.id)
                    current_neighbour.optimus_path = new_optimus
                    if debug:
                        print("Found new minimum of " + str(possible)
                              + " with neighbour " + str(current_neighbour.id))
            else:
                # we're on 1st node
                current_neighbour.current_value = weight_matrix[node.id][current_neighbour.id]
                current_neighbour.optimus_path.append(node.id)
                if debug:
                    print("Found new minimum of " + str(weight_matrix[node.id][current_neighbour.id]))
        node.completed = True
        node.remove_from_neighbour()
        if debug:
            print("Node " + str(node.id) + " Done. \n\n")


main()

from module.WeightMatrix import WeightMatrix
from module.Node import Node

undirected_graph = True
debug = False


def main():
    print("Main")
    # nodes = prepare_graph()
    # dijkstra(nodes=nodes, start=3, finish=2)


# Custom preparation of the graph. Future release will allow graphic interface
def prepare_graph():
    nodes = [0, 1, 2, 3, 4, 5]
    weight_matrix = WeightMatrix(len(nodes))
    weight_matrix = weight_matrix.matrix

    for node in nodes:
        nodes[node] = Node(node)

    nodes[0].add_neighbour(nodes[1], 4, weight_matrix, undirected_graph)
    nodes[0].add_neighbour(nodes[3], 1, weight_matrix, undirected_graph)
    nodes[0].add_neighbour(nodes[2], 3, weight_matrix, undirected_graph)
    nodes[1].add_neighbour(nodes[2], 1, weight_matrix, undirected_graph)
    nodes[1].add_neighbour(nodes[3], 2, weight_matrix, undirected_graph)
    nodes[2].add_neighbour(nodes[3], 4, weight_matrix, undirected_graph)
    nodes[2].add_neighbour(nodes[4], 3, weight_matrix, undirected_graph)
    nodes[3].add_neighbour(nodes[4], 1, weight_matrix, undirected_graph)
    nodes[3].add_neighbour(nodes[5], 10, weight_matrix, undirected_graph)
    nodes[4].add_neighbour(nodes[5], 1, weight_matrix, undirected_graph)

    return nodes


def dijkstra_with_start(nodes, start):
    for node in nodes:
        if node.id == start:
            start_node = node
            nodes.remove(node)
            nodes.insert(0, start_node)


def dijkstra(nodes, weight_matrix, start=None, finish=None):
    if start is not None:
        dijkstra_with_start(nodes, start)
    apply_dijkstra(nodes, weight_matrix)
    if finish is None:
        for node in nodes:
            node.print_path()
    else:
        for node in nodes:
            if node.id == finish:
                # print("printing the result")
                # print(node.optimal_path)
                # print(node.current_value)
                return node.current_value


def apply_dijkstra(nodes, weight_matrix):
    for node in nodes:
        if debug:
            print("Node " + str(node.id))
        for current_neighbour in node.neighbour:
            if node.current_value is not None:
                possible = node.current_value + weight_matrix[node.id][current_neighbour.id]
                if (current_neighbour.current_value is None) or (possible < current_neighbour.current_value):
                    current_neighbour.current_value = possible
                    new_optimus = node.optimal_path.copy()
                    new_optimus.append(current_neighbour.id)
                    current_neighbour.optimal_path = new_optimus
                    if debug:
                        print("Found new minimum of " + str(possible)
                              + " with neighbour " + str(current_neighbour.id))
            else:
                # we're on 1st node
                current_neighbour.current_value = weight_matrix[node.id][current_neighbour.id]
                current_neighbour.optimal_path.append(node.id)
                current_neighbour.optimal_path.append(current_neighbour.id)
                if debug:
                    print("Found new minimum of " + str(weight_matrix[node.id][current_neighbour.id])
                          + " with neighbour " + str(current_neighbour.id))
        node.completed = True
        node.remove_from_neighbour()
        if debug:
            print("Node " + str(node.id) + " Done. \n\n")


main()

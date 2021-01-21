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


def dijkstra(nodes, weight_matrix, start=None, finish=None):
    if start is None:
        apply_dijkstra(nodes[0], weight_matrix)
    else:
        apply_dijkstra(start, weight_matrix)
    if finish is None:
        for node in nodes:
            node.print_path()
    else:
        for node in nodes:
            if node.id == finish:
                # print("printing the result")
                print(node.optimal_path)
                # print(node.current_value)
                return node.current_value


def apply_dijkstra(starting_node, weight_matrix):
    next_node = None
    current_node = starting_node
    for neighbour in current_node.neighbour:
        if not neighbour.completed:
            next_node = neighbour
            # Inserted Here
            if current_node.current_value is not None:
                possible = current_node.current_value + weight_matrix[current_node.id][neighbour.id]
                if (neighbour.current_value is None) or (possible < neighbour.current_value):
                    neighbour.current_value = possible
                    new_optimus = current_node.optimal_path.copy()
                    new_optimus.append(neighbour.id)
                    neighbour.optimal_path = new_optimus
                    if debug:
                        print("Found new minimum of " + str(possible)
                              + " with neighbour " + str(neighbour.id))
            else:
                # we're on 1st node
                neighbour.current_value = weight_matrix[current_node.id][neighbour.id]
                neighbour.optimal_path.append(current_node.id)
                neighbour.optimal_path.append(neighbour.id)
                if debug:
                    print("Found new minimum of " + str(weight_matrix[current_node.id][neighbour.id])
                          + " with neighbour " + str(neighbour.id))
            # compute dijkstra
            # End inserted here
    current_node.completed = True
    # node.remove_from_neighbour()
    if next_node is not None:
        apply_dijkstra(next_node, weight_matrix)


main()

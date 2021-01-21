# Setting main parameter

undirected_graph = True
debug = False


# Custom preparation of the graph. Future release will allow graphic interface


def dijkstra(nodes, weight_matrix, start=None, finish=None):
    if start is None:
        apply_dijkstra(nodes[0], weight_matrix)
    else:
        apply_dijkstra(nodes[start], weight_matrix)
    if finish is None:
        for node in nodes:
            node.print_path()
    else:
        for node in nodes:
            if node.id == finish:
                print(node.optimal_path)
                # print(node.current_value)
                return node.current_value


def apply_dijkstra(starting_node, weight_matrix):
    next_nodes = []
    current_node = starting_node
    if debug:
        print("analyzing node " + str(current_node.id))
    for neighbour in current_node.neighbour:
        if not neighbour.completed:
            next_nodes.append(neighbour)
            # Inserted Here
            if current_node.current_value is not None:
                possible = current_node.current_value + weight_matrix[current_node.id][neighbour.id]
                if neighbour.current_value is None:
                    neighbour.current_value = possible
                    neighbour.optimal_path = current_node.optimal_path.copy()
                    neighbour.optimal_path.append(neighbour.id)
                if possible <= neighbour.current_value:
                    new_optimal = current_node.optimal_path.copy()
                    new_optimal.append(neighbour.id)
                    # save new path just if it's shorter, giving that we have the same value for the path
                    if possible == neighbour.current_value:
                        if len(new_optimal) < len(neighbour.optimal_path):
                            neighbour.optimal_path = new_optimal
                    else:
                        neighbour.optimal_path = new_optimal
                    neighbour.current_value = possible
                    if debug:
                        print("Found new minimum of " + str(possible) + " with neighbour " + str(neighbour.id))
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
    for neigh in next_nodes:
        apply_dijkstra(neigh, weight_matrix)

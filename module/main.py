# Setting main parameter

undirected_graph = True
debug = False


# Custom preparation of the graph. Future release will allow graphic interface

def dijkstra(graph, start_id, finish_id=None):
    apply_dijkstra(graph.nodes[start_id], graph.weight_matrix)
    if finish_id is None:
        for node in graph.nodes:
            node.print_path()
    else:
        for node in graph.nodes:
            if node.id == finish_id:
                print(node.optimal_path)
                return node.current_value


def apply_dijkstra(starting_node, weight_matrix):
    next_nodes = []
    current_node = starting_node
    if debug:
        print("analyzing node " + str(current_node.id))
    for neighbour in current_node.neighbour:
        if not neighbour.completed:
            next_nodes.append(neighbour)
            if current_node.current_value is not None:
                possible = current_node.current_value + weight_matrix[current_node.id][neighbour.id]
                new_optimal_possible = [*current_node.optimal_path, neighbour.id]
                # If the neighbour of the current node has never been visited before
                if neighbour.current_value is None:
                    neighbour.current_value = possible
                    neighbour.optimal_path = new_optimal_possible
                elif possible <= neighbour.current_value:
                    # save new path just if it's shorter, giving that we have the same value for the path
                    if possible == neighbour.current_value:
                        if len(new_optimal_possible) < len(neighbour.optimal_path):
                            neighbour.optimal_path = new_optimal_possible
                    else:
                        neighbour.optimal_path = new_optimal_possible
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
    current_node.completed = True
    for neigh in next_nodes:
        apply_dijkstra(neigh, weight_matrix)

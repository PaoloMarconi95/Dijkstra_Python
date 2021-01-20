class Node:
    def __init__(self, id, neighbour=None, completed=False, optimus_path=None, current_value=-1):
        if neighbour is None:
            neighbour = []
        if optimus_path is None:
            optimus_path = []
        self.id = id
        self.neighbour = neighbour
        self.completed = completed
        self.current_value = current_value
        self.optimus_path = optimus_path

    def add_neighbour(self, new_neighbour, weight, weight_matrix, undirected_graph):
        self.neighbour.append(new_neighbour)
        weight_matrix[self.id][new_neighbour.id] = weight
        if undirected_graph:
            new_neighbour.add_neighbour_redundant(new_neighbour=self, weight=weight,
                                                  weight_matrix=weight_matrix)

    def add_neighbour_redundant(self, new_neighbour, weight, weight_matrix):
        self.neighbour.append(new_neighbour)
        weight_matrix[self.id][new_neighbour.id] = weight

    def remove_from_neighbour(self):
        for neig in self.neighbour:
            if not neig.completed:
                neig.neighbour.remove(self)

    # Debug only
    def print_state(self):
        print('Current Node ' + str(self.id))
        print('Completed : ' + str(self.completed))
        print('neighbour of current node: ')
        for neigh in self.neighbour:
            print(str(neigh.id), end=", ")
        print("")

    def print_path(self):
        print('Current Node : ' + str(self.id) +
              '\nPath : ' + str(self.current_value) +
              '\nOptimus Path: ' + str(self.optimus_path))
        print("\n")

class Node:
    def __init__(self, id, neighbour=None, completed=False, optimal_path=None, current_value=None):
        if neighbour is None:
            neighbour = []
        if optimal_path is None:
            optimal_path = []
        self.id = id
        self.neighbour = neighbour
        self.completed = completed
        self.current_value = current_value
        self.optimal_path = optimal_path

    def add_neighbour(self, new_neighbour):
        self.neighbour.append(new_neighbour)

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
              '\nOptimal Path: ' + str(self.optimal_path))
        print("\n")

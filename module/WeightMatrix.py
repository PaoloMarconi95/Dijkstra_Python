import numpy as np

class WeightMatrix:

    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.matrix = np.zeros((self.n_nodes, self.n_nodes))
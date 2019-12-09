#!/usr/bin/env python
from mlxtend.data import loadlocal_mnist
import numpy as np
import sklearn.metrics as sk

class Neuron:
    def __init__(self, number_of_inputs):
        self.weight = np.random.rand(number_of_inputs)
        self.output = np.array()
        self.bias =

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))





   for key in unvisited:
        visited[str(key)] = -1
    return(visited)
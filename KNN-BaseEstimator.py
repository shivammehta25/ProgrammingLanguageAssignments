#!/usr/bin/env python
from sklearn.base import BaseEstimator
from sklearn.neighbors import KDTree
import math
import numpy as np
from random import shuffle
from sklearn.metrics import f1_score

class KNearestNeighbour(BaseEstimator):
    def __init__(self, neighbors=5):
        self.neighbors = neighbors
        self.training_set = []
        self.test_set = []

    def fit(self):
        X, Y = self.split_data_and_labels(self.training_set)
        self.tree = KDTree(X, leaf_size=2)
        self.labels = Y
        return self

    def predict(self, X):
        # Predict the class labels for the provided data
        X, true_labels = self.split_data_and_labels(X)
        dist,  ind = self.tree.query(X, k=self.neighbors)
        predictions = []
        # print(ind)
        for x in range(len(X)):
            labels = {0: 0, 1: 0}  # dict of possible labels -- 0 and 1
            for i in range(len(ind[x])):
                label = self.labels[ind[x][i]]
                labels[label] += 1
            pred = max(labels, key=labels.get)
            predictions.append(pred)
        print("F1 score is equal to " + repr(f1_score(true_labels, predictions, average='weighted')))
        return predictions

    def load_dataset(self, filename, split):
        with open(filename) as f:
            dataset = f.readlines()
        shuffle(dataset)
        for x in range(len(dataset) - 1):
            dataset[x].rstrip('\n')
            ex = dataset[x].split()
            for y in range(3):
                ex[y] = float(ex[y].replace(',', '.'))
            if x < split * (len(dataset) - 1):
                self.training_set.append(ex)
            else:
                self.test_set.append(ex)
        return self.training_set, self.test_set

    def split_data_and_labels(self, dataset):
        X = []
        Y = []
        for x in dataset:
            X.append(x[0:2])
            Y.append(x[2])
        return X, Y


def main():
    model = KNearestNeighbour(neighbors=5)
    model.load_dataset('/Users/shivam/PycharmProjects/ProgrammingLanguageTask1/data/KNN_dataset.txt', 0.66)
    model.fit()
    model.predict(model.test_set)

if __name__ == '__main__':
    main()
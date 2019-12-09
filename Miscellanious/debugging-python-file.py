import pandas as pd
import numpy as np
from math import sqrt, pow
import operator
import random
import csv



data = list(csv.reader(open('/Users/shivam/PycharmProjects/ProgrammingLanguageTask1/data/KNN_dataset.txt', 'r'), delimiter='\t'))

def loadDataset(split, training_set, testSet):
    for x in range(len(data) - 1):
        for y in range(2):
            data[x][y] = float(data[x][y])
        if random.random() < split:
            training_set.append(data[x])
        else:
            testSet.append(data[x])


def find_euclidian_distance(p2, p1, length):
    distance = 0
    for i in range(length):
        distance += pow((p2[i] - p1[i]), 2)
    return sqrt(distance)


def get_neighbours(training_dataset, test_instances, k):
    distance = []
    length = len(test_instances) - 1
    for train_data in training_dataset:
        distance.append((train_data, find_euclidian_distance(train_data, test_instances, length)))
    distance.sort(key=operator.itemgetter(1))
    neighbours = []
    for i in range(k):
        neighbours.append(distance[i])
    return neighbours


def get_response(neighbours):
    responses = {}
    for i in range(len(neighbours)):
        output = neighbours[i][0][-1]
        if output in responses:
            responses[output] += 1
        else:
            responses[output] = 1
    responses_sorted = sorted(responses.items(), key=lambda kv: kv[1], reverse=True)
    return responses_sorted[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


predictions = []
k = 5
training_set = []
test_set = []
loadDataset(0.80, training_set, test_set)
for x in range(len(test_set)):
    neighbours = get_neighbours(training_set, test_set[x], k)
    response = get_response(neighbours)
    predictions.append(response)
    print('Predcited : {0} Actual {1}'.format(response, test_set[x]))

print(getAccuracy(test_set, predictions))

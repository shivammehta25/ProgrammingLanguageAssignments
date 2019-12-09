#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fountainActivation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import defaultdict


def fountainActivation(a):
    # Write your code here
    information = populate_information(a)
    print(information)
    n_t = 1
    current_set = information[0]
    print('{} {}'.format(0, current_set))
    current_elements = defaultdict(int)
    # for i in current_set:
    #     current_elements[i] += 1
    #
    # print(current_elements)
    print('len_info : {}'.format(len(information)))
    for i in range(1, len(information)):
        print(i, end=' ')
        loop_set = information[i]
        next_set = current_set.intersection(loop_set)
        print(next_set)
        if not next_set:
            print('Information : {}'.format(information[i-1]))
            current_set = information[i]
            n_t += 1

    return n_t






def populate_information(a):
    fountains = dict(enumerate(a))
    information = defaultdict(set)
    for i in range(len(fountains)):
        fountain_number = i
        fountain_range = fountains[i]
        print(fountain_number, fountain_range)
        for j in range(len(fountains)):
            if fountain_number <= j + fountains[j] and fountain_number >= j - fountains[j]:
                if fountains[j]:
                    information[i].add(j)
                else:
                    information[i].add(12345678)
    return information


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = fountainActivation(a)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

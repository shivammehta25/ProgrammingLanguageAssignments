#!/usr/bin/env python

#   Count internal nodes of a tree Recursively

class Node:
    counter = 0
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def print_tree(self, node):
        if not node:
            return 0
        self.print_tree(node.left)
        if node.left:
            Node.counter +=1
        print(node.key)
        self.print_tree(node.right)





if name == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)

    root.print_tree(root)
    print('Counter : {}'.format(Node.counter))
#!/usr/bin/env python



class DT:
    def __init__(self, X, Y, max_depth=10):
        self.X = X
        self.Y = Y
        self.max_depth = max_depth
        self.n = len(X)
        self.features = len(X[0])
        self.classes = np.unique(Y)
        self.tree = []


    def information_gain_gini(self, groups, y_groups):
        total_values = sum(len(g) for g in groups)
        score = 0.0
        for i in range(len(groups)):
            group = groups[i]
            y_group = y_groups[i]
            group_size = float(len(group))
            if group_size == 0.0:
                continue
            gini_score_group = 0.0
            for i in self.classes:
                propotion = (y_group == i).sum() / group_size
                gini_score_group += propotion * propotion

            score += ( 1.0 - gini_score_group ) * ( group_size/total_values)
        return score


    def do_split_and_test(self, column_index, value, dataset, y_data):
        left = []
        right = []
        y_left = []
        y_right = []

        for i in range(len(dataset)):
            if dataset[i][column_index] < value:
                left.append(dataset[i])
                y_left.append(y_data[i])
            else:
                right.append(dataset[i])
                y_right.append(y_data[i])

        return ( np.array(left), np.array(right) ) , ( np.array(y_left), np.array(y_right) )


    def generate_best_split(self, dataset, y_data):
        best_gini_score, best_index, best_value, best_groups = float("inf"), 999, 999, []
        for index in range(self.features):
            i = 0
            for row in dataset:
                i+=1
                groups, y_groups = self.do_split_and_test(index, row[index], dataset, y_data)
                gini_score = self.information_gain_gini(groups, y_groups)
                if gini_score < best_gini_score:
                    best_gini_score, best_index, best_value, best_groups, best_y_groups  = gini_score, index, row[index], groups, y_groups

        return {'index':best_index, 'value':best_value, 'groups':best_groups, 'y_groups' : best_y_groups}


    def gen_terminal(self, group):
        group = group.tolist()
        return max(np.unique(group), key=group.count)


    def split(self, node, depth):
        left, right = node['groups']
        y_left, y_right = node['y_groups']
        del node['groups']
        del node['y_groups']

        if not len(left) or not len(right):
            node['left'] = node['right'] = self.gen_terminal(np.append(y_left, y_right))
            return

        if depth >= self.max_depth:
            node['left'], node['right'] = self.gen_terminal(y_left), self.gen_terminal(y_right)
            return


        node['left'] = self.generate_best_split(left, y_left)
        self.split(node['left'], depth+1)

        node['right'] = self.generate_best_split(right, y_right)
        self.split(node['right'], depth+1)


    def generate_tree(self):
        root = self.generate_best_split(self.X, self.Y)
        self.split(root, 1)
        self.tree = root


    def accuracy(self):
        accuracy = 0
        for i in range(len(self.y_predicted)):
            if int(self.y_predicted[i]) == int(self.y_test[i]):
                accuracy += 1

        return float(accuracy * 100/len(self.y_predicted))


    def recursive_predict(self, node, row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.recursive_predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.recursive_predict(node['right'], row)
            else:
                return node['right']


    def predict(self,test_x, test_y):
        self.y_predicted = []
        self.y_test = test_y
        self.x_test = test_x
        for row in test_x:
            self.y_predicted.append(self.recursive_predict(self.tree, row))


        return self.y_predicted





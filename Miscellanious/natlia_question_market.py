#!/usr/bin/env python


import sys

path_to_file = 'goods.mt'


class Good:
    def __init__(self):
        self.name = ''
        self.category = ''
        self.price = 0
        self.rating = 0

    def __str__(self):
        return 'Name: {} \nCategory: {} \nPrice : ${} \nRating: {}\n'.format(self.name, self.category, self.price, self.rating)


class Goods:
    def __init__(self):
        self.goods = []
        self.get_all_items()

    def get_all_items(self):
        with open(path_to_file, 'r') as file:
            for line in file:
                if "Name" in line:
                    good = Good()
                    good.name = line.split(':')[1].strip()
                elif "Category" in line:
                    good.category = line.split(':')[1].strip()
                elif "Price" in line:
                    good.price = int(line.split(':')[1].replace('$', '').strip())
                elif "Rating" in line:
                    good.rating = int(line.split(':')[1].strip())
                    self.goods.append(good)

    def write_all_items(self):
        with open(path_to_file, 'w') as file:
            for good in self.goods:
                file.write("Name: {0}\nCategory: {1}\nPrice: ${2}\nRating: {3}\n\n".format(good.name, good.category, good.price, good.rating))

    def add(self, good):
        if good.name in [good.name for good in self.goods]:
            print('Item with the same name already exists. Cannot add item')
        else:
            self.goods.append(good)
            self.write_all_items()



    def remove(self, name):
        if name not in [good.name for good in self.goods]:
            print('Cannot find item with that name.')
        else:
            for g in self.goods:
                if g.name == name:
                    self.goods.remove(g)
            self.write_all_items()
            self.get_all_items()


    def best(self, category):
        if category not in [good.category for good in self.goods]:
            print('Product in this category cannot be found')
        else:
            min_price = min([good.price for good in self.goods])
            for good in self.goods:
                if good.price == min_price:
                    print(good)

    def recommend(self, price, category):
        filtered_list = list(filter(lambda good: True if good.category == category and good.price <= price else False, self.goods))
        if not filtered_list:
            print('Product in this category cannot be found')
        else:
            max_price = max(good.price for good in filtered_list)
            for good in filtered_list:
                if good.price == max_price:
                    print(good)



def menu(args):
    goods = Goods()
    if not args:
        print('No Options Supplied')
    else:
        if args[1] == 'add':
            good = Good()
            good.name = args[2]
            good.category = args[3]
            good.price = args[4]
            good.rating = args[5]
            goods.add(good)
        elif args[1] == 'remove':
            name = args[2]
            goods.remove(name)
        elif args[1] == 'best':
            category = args[2]
            goods.best(category)
        elif args[1] == 'recommend' :
            price = int(args[2])
            category = args[3]
            goods.recommend(price,category)
        else:
            print('Invalid Option Selected')

if __name__ == '__main__':
    menu(sys.argv)








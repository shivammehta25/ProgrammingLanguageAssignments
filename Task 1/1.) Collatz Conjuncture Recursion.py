#!/bin/usr/env python


def collatz_conjuncture(number):
    print(int(number))
    if number == 1:
        return 1
    elif number % 2 == 0:
        collatz_conjuncture(number / 2)
    else:
        collatz_conjuncture(3 * number + 1)


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    collatz_conjuncture(number)

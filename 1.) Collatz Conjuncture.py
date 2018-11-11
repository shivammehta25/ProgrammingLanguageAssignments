#!/bin/usr/env python


def main():
    number = int(input('Enter the number: '))

    while number != 1:
        print(int(number))
        if number % 2 == 0:
            number /= 2
        else:
            number = (3 * number) + 1

        number = int(number)
    print(number)


if __name__ == '__main__':
    main()

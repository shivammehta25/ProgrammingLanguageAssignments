#!/usr/bin/env python3


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real, self.imaginary * other.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        return '{0} + {1}i'.format(self.real, self.imaginary) if self.real else '{0}i'.format(self.imaginary if self.imaginary else '')


def main():
    a = ComplexNumber(0, 9)
    b = ComplexNumber(10, 5)
    c = ComplexNumber(5, 2)
    print('Str: a = {0} , b = {1} , c = {2} '.format(a, b, c))
    print('Addition: {0}'.format(a+b))
    print('Subtraction: {0}'.format(b-a))
    print('Multiplication: {0}'.format(a*b))
    print('Equality For True: {0}'.format(a == c))
    print('Equality for False: {0}'.format(a == b))


if __name__ == '__main__':
    main()
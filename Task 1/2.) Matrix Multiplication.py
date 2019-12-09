#!/bin/usr/env python


first_matrix_file_name = 'a.txt'
second_matrix_file_name = 'b.txt'
output_matrix_file_name = 'c.txt'


def validate_matrix_for_multiplication(a, b):
    return len(b) == len(a[0])


def multiply_matrix(a, b):
    final_matrix = [[0 for i in range(len(a))] for j in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                final_matrix[i][j] += a[i][k] * b[k][j]
    return final_matrix


def main():
    a = populate_array_from_file(first_matrix_file_name)
    b = populate_array_from_file(second_matrix_file_name)

    if not validate_matrix_for_multiplication(a, b):
        raise ArithmeticError('Matrix Cannot be multiplied!')

    if ( not validate_square_matrix(a)) or not validate_square_matrix(b):
        raise ArithmeticError('Matrix are not square matrices.')

    c = multiply_matrix(a, b)
    print_it = lambda x: ' '.join(map(str, x))

    with open(output_matrix_file_name, 'w') as output_file:
        output_file.write('\n'.join(print_it(x) for x in c))


def validate_square_matrix(a):
    is_square = lambda m: all(len(row) == len(m) for row in m)
    return is_square(a)


def populate_array_from_file(filename):
    final_array = list()
    with open(filename, 'r') as file:
        for line in file:
            final_array.append([int(x) for x in line.split()])

    return final_array


if __name__ == '__main__':
    main()

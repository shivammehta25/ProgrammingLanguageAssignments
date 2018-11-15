#!/bin/usr/env python
import string

class Configuration:
    file_name = 'text.txt'
    output_file = 'stat.txt'


def main():
    word_counter = {}
    with open(Configuration.file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isalpha():
                    if word in word_counter:
                        word_counter[word] += 1
                    else:
                        word_counter[word] = 1

    with open(Configuration.output_file, 'w') as file:
        for word in word_counter:
            file.write('{0} {1}\n'.format(word, word_counter[word]))


if __name__ == '__main__':
    main()

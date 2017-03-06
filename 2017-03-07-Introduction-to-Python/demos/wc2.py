# Note: This script is just an illustration. It contains a very simple solution
# to the problem, which is far from perfect.

import argparse
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Prints the number of lines and words in file.'
    )
    parser.add_argument('file_path', metavar='FILE')
    return parser.parse_args(args[1:])

def count_lines_and_words(file):
    lines = 0
    words = 0
    for line in file:
        lines += 1
        for word in line.split(' '):
            if word.strip():
                words += 1
    return lines, words

def print_lines_and_words(lines, words):
    print(lines, words)

def main():
    args = parse_args(sys.argv)
    with open(args.file_path, 'r') as f:
        lines, words = count_lines_and_words(f)
    print_lines_and_words(lines, words)

if __name__ == '__main__':
    main()

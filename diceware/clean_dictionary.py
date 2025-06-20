#!/usr/bin/env python3

import argparse
import sys
import os
import re

parser = argparse.ArgumentParser(prog='clean_dictionary.py', description='Utility script to clean a dictionary files of proper nouns and words with apostrophes.')

parser.add_argument('-i', '--input', '--input-file', help='Dictionary file to clean', metavar='PATH', type=str, required=True)
parser.add_argument('-o', '--output', '--output-file', help='File to write cleaned wordlist to', metavar='PATH', type=str, required=False, default='cleaned_list.txt')

if __name__ == '__main__':
    args = parser.parse_args()

    if not os.access(args.input, os.F_OK):
        print('ERROR! Could not find input file.', file=sys.stderr)
        exit(1)

    words_list = []

    with open(args.input, 'r') as input_file:
        words_list = input_file.readlines()

    with open(args.output, 'w') as output_file:
        for word in words_list:
            word_str = word.strip()
            # Exclude words containing numbers, capital letters,
            # or nonalphabetic characters.
            # e.g., exclude "20th", "yo-yo", and "writer's"
            if not re.search(r'[A-Z\W0-9]+', word_str):
                print(word_str, file=output_file)

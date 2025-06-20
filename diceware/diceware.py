#!/usr/bin/env python3

import argparse
import sys
import random

parser = argparse.ArgumentParser(prog='diceware.py', description='Small \"diceware\" program to pseudorandomly generate a passphrase from a dictionary file.')

parser.add_argument('-i', '--input', '-l', '--list', '--input-list', help='Input wordlist/dictionary to generate passphrase from', required=True, type=str, metavar='FILE')
parser.add_argument('-o', '--output', help='File to write passphrase to (default: stdout)', required=False, type=str, metavar='FILE')
parser.add_argument('-n', '--num-words', help='Number of words to generate in passphrase', required=False, type=int, metavar='NUM', default=4)
parser.add_argument('--min-length', help='Minimum word length for each word in passphrase', required=False, type=int, default=1, metavar='LENGTH')
parser.add_argument('--no-spaces', help='Print the passphrase without spaces', action='store_true', required=False)

if __name__ == '__main__':
    args = parser.parse_args()
    
    outfile = sys.stdout

    if (args.output):
        try: 
            outfile = open(args.output, 'a')
        except:
            print("WARNING: could not open output file! Reverting to stdout.", file=sys.stderr)

    with open(args.input, 'r') as input_wordlist:
        wordlist = input_wordlist.readlines()
        list_len = len(wordlist)

        for i in range(0, args.num_words):
            next_word = wordlist[random.randrange(0, list_len, 1)].strip()

            if len(next_word) >= args.min_length:
                print(next_word, file=outfile, end='')
                
                if not (args.no_spaces):
                    print('', end=' ')

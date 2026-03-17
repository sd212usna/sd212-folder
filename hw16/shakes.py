#!/usr/bin/env python3

from argparse import ArgumentParser
from urllib.request import urlopen

def count(url, length):
    c = 0
    with urlopen(url) as f:
        line = f.readline()
        while line:
            for word in line.decode().split():
                if len(word) == length:
                    c += 1
            line = f.readline()
    print(f'{length}: {c}')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('length', type=int)
    args = parser.parse_args()
    count('http://faculty.cs.usna.edu/~roche/shakespeare.txt', args.length)

import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]

for line in lines:
    print(line)

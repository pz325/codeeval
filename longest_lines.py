'''
https://www.codeeval.com/open_challenges/2/

INPUT SAMPLE:

Your program should read an input file (the first argument to your program will be a path to a filename). The first line contains the value of the number 'N' followed by multiple lines. You may assume that the input file is formatted correctly and the number on the first line i.e. 'N' is a valid positive integer. E.g.

2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE:

The 'N' longest lines, newline delimited. Ignore all empty lines in the input. Ensure that there are no trailing empty spaces on each line you print. Also ensure that the lines are printed out in decreasing order of length i.e. the output should be sorted based on their length. E.g.

San Francisco
Hello World

'''

def longestLines(fileName):
    f = open(fileName)
    N = int(f.readline())
    lines = list(f)
    for outLine in sorted(lines, key=lambda l: len(l), reverse=True)[:N]:
        print(outLine)

# longestLines('test')

import sys
longestLines(sys.argv[1])

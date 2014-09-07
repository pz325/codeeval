'''
https://www.codeeval.com/open_challenges/38/

You are given a number N and a string S. Print all of the possible ways to write a string of length N from the characters in string S, comma delimited in alphabetical order.

INPUT SAMPLE:

The first argument will be the path to the input filename containing the test data. Each line in this file is a separate test case. Each line is in the format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop
OUTPUT SAMPLE:

Print all of the possible ways to write a string of length N from the characters in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp
'''

import itertools

def stringList(test):
    (N, s) = test.strip().split(',')
    N = int(N)
    chSet = set()
    for c in s:
        chSet.add(c)
    outStrs = []
    for s in itertools.product(sorted(chSet), repeat=N):
        outStrs.append(''.join(s))
    print(','.join(outStrs))

# stringList('2,tt')
# stringList('2,ab')
# stringList('3,pop')

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    if test != '': stringList(test)

test_cases.close()

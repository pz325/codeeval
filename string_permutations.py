'''
https://www.codeeval.com/open_challenges/14/

Write a program to print out all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.

INPUT SAMPLE:

Your program should accept as its first argument a path to a file containing an input string, one per line. E.g.

hat
abc
Zu6
OUTPUT SAMPLE:

Print to stdout, permutations of the string, comma separated, in alphabetical order. E.g.

aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6
'''

import itertools
def stringPermutations(test):
    chSet = set()
    for c in test.strip():
        chSet.add(c)
    outStrs = []
    for s in itertools.permutations(sorted(chSet)):
        outStrs.append(''.join(s))
    print(','.join(outStrs))


# stringPermutations('hat')
# stringPermutations('abc')
# stringPermutations('Zu6')

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    if test != '': stringPermutations(test)
    # ...

test_cases.close()


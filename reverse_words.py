'''
https://www.codeeval.com/open_challenges/8/

INPUT SAMPLE:

The first argument will be a path to a filename containing multiple sentences, one per line. Possibly empty lines too. E.g.

Hello World
Hello CodeEval
OUTPUT SAMPLE:

Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print. E.g.

World Hello
CodeEval Hello
'''

def reverseWords(line):
    line = line.strip()
    if line != '':
        words = line.split(' ')
        revWords = words[::-1]
        print(' '.join(revWords))

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    reverseWords(test)
    # ...

test_cases.close()

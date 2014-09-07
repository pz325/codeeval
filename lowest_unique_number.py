'''
https://www.codeeval.com/open_challenges/103/

There is a game where each player picks a number from 1 to 9, writes it on a paper and gives to a guide. A player wins if his number is the lowest unique. We may have 10-20 players in our game.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.

You're a guide and you're given a set of numbers from players for the round of game. E.g. 2 rounds of the game look this way:

3 3 9 1 6 5 8 1 5 3
9 2 9 9 1 8 8 8 2 1 1
OUTPUT SAMPLE:

Print a winner's position or 0 in case there is no winner. In the first line of input sample the lowest unique number is 6. So player 5 wins.

5
0
'''

def lowestUniqueNumber(test):
    test = test.strip()
    if len(test) > 0:
        numbers = [int(i) for i in test.split(' ')]
        decks = [[] for i in range(11)]
        for i in range(1, len(numbers)+1):
            decks[numbers[i-1]].append(i)
        for i in range(1, 10):
            if len(decks[i]) == 1:
                print(decks[i][0])
                return
        print(0)

# lowestUniqueNumber('3 3 9 1 6 5 8 1 5 3')
# lowestUniqueNumber('9 2 9 9 1 8 -8 8 2 1 1')

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    lowestUniqueNumber(test)
    # ...

test_cases.close()
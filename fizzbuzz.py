'''
https://www.codeeval.com/open_challenges/1/

INPUT SAMPLE:

Your program should read an input file (provided on the command line) which contains multiple newline separated lines. Each line will contain 3 numbers which are space delimited. The first number is first number to divide by ('A' in this example), the second number is the second number to divide by ('B' in this example) and the third number is where you should count till ('N' in this example). You may assume that the input file is formatted correctly and is the numbers are valid positive integers. E.g.


3 5 10
2 7 15
OUTPUT SAMPLE:

Print out the series 1 through N replacing numbers divisible by 'A' by F, numbers divisible by 'B' by B and numbers divisible by both as 'FB'. Since the input file contains multiple sets of values, your output will print out one line per set. Ensure that there are no trailing empty spaces on each line you print. E.g.

1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
Constraints: 
The number of test cases <= 20 
"A" is in range [1, 20] 
"B" is in range [1, 20] 
"N" is in range [21, 100]
'''

def fizzbuzz(test):
    (A, B, N) = test.split(' ')
    A, B, N = int(A), int(B), int(N)
    seq = []
    for i in range(1, N+1):
        if i % A == 0 and i % B == 0:
            seq.append('FB')
        else:
            if i % A == 0:
                seq.append('F')
            elif i % B == 0:
                seq.append('B')
            else:
                seq.append(str(i))
    print(' '.join(seq))


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    fizzbuzz(test)
    # ...

test_cases.close()

# fizzbuzz('10 1 58')
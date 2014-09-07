'''
https://www.codeeval.com/open_challenges/28/

CHALLENGE DESCRIPTION:

You are given two strings. Determine if the second string is a substring of the first (Do NOT use any substr type library function). The second string may contain an asterisk(*) which should be treated as a regular expression i.e. matches zero or more characters. The asterisk can be escaped by a \ char in which case it should be interpreted as a regular '*' character. To summarize: the strings can contain alphabets, numbers, * and \ characters.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The input file contains two comma delimited strings per line. E.g.

Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young
OUTPUT SAMPLE:

If the second string is indeed a substring of the first, print out a 'true'(lowercase), else print out a 'false'(lowercase), one per line. E.g.

true
true
true
false
'''

def substring(s, t):
    '''
    return Tuple (True/False, i)
    '''
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
            if j == len(t):
                return (True, i)
        else:
            i += 1
            j = 0
    return (False, i)

def substringWithAsterisk(s, t):
    # search '\*'
    i, tmp, tokens = 0, [], []
    while i < len(t):
        if t[i] != '*':
            tmp.append(t[i])
        else:
            if i > 0 and t[i-1] == '\\':
                tmp[-1] = '*'
            else:
                tokens.append(''.join(tmp))
                tmp = []
        i += 1
    tokens.append(''.join(tmp))
    # print(tokens)
    i, j, strFound = 0, 0, True
    while i < len(tokens) and strFound:
        if len(tokens[i]) == 0:
            strFound = True
        else:
            strFound, j = substring(s[j:], tokens[i])
        i += 1
    return strFound

def stringSearch(test):
    s, t = test.strip().split(',')
    if substringWithAsterisk(s, t): 
        # print('{test} {s} {t}: true'.format(test=test, s=s, t=t))
        print('true')
    else:
        # print('{test} {s} {t}: false'.format(test=test, s=s, t=t))
        print('false')
        

# stringSearch('Hello,ell')
# stringSearch('This is good, is')
# stringSearch('CodeEval,C*Eval')
# stringSearch('Old,Young')
# stringSearch('C*odeEval,*')
# stringSearch('CodeEval,Code*')
# stringSearch('CodeEval,Co**val')
# stringSearch('CodeEval,Co*val')


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    stringSearch(test)
    # ...

test_cases.close()

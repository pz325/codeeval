'''
https://www.codeeval.com/open_challenges/25/

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print the odd numbers from 1 to 99, one number per line. 
'''
def oddNumbers():
    for i in range(1, 100, 2):
        print(i)

oddNumbers()
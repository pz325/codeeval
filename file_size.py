'''
https://www.codeeval.com/open_challenges/26/

INPUT:

The first argument to your program has the path to the file you need to check the size of.

OUTPUT SAMPLE:

Print the size of the file in bytes. E.g.

55
'''
import sys
import os
print(os.path.getsize(sys.argv[1]))

import math
import os
import random
import re
import sys
def solve(s):
    str = ""
    mode = 1
    for c in s:
    	d = c
    	if c == ' ':
    		mode = 1
    	elif mode == 1:
    		d = c.upper()
    		mode = 0
    	str += d
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

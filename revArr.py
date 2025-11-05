#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Method 1: Using slicing (most Pythonic)
    return a[::-1]
    
    # Method 2: Using built-in reversed() function
    # return list(reversed(a))
    
    # Method 3: Using reverse() method (modifies original)
    # a.reverse()
    # return a
    
    # Method 4: Manual reversal with two pointers
    # left, right = 0, len(a) - 1
    # while left < right:
    #     a[left], a[right] = a[right], a[left]
    #     left += 1
    #     right -= 1
    # return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
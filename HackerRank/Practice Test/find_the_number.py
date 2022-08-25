#Given an unsorted array n, find if k is present
#Return a string "YES" or "NO"
#First list gives number of elements (-1?)
#Each subsequent line gives integer

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k

def findNumber(arr, k):
    #Convert array to set
    numset = set()
    for i in arr:
        numset.add(i)
    
    #Search set for k
    if k in numset:
        return "YES"
    else:
        return "NO"
    

print(findNumber([1, 2, 3, 4, 5], 2))

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findNumber(arr, k)

    fptr.write(result + '\n')

    fptr.close()
    """
#!/bin/python3

import math
import os
import random
import re
import sys

def median(X):
    #return sum(X) / len(X)
    X = sorted(X)
    if(len(X) % 2 == 0): 
        median = (X[int(len(X)/2)]  + X[int(len(X)/2) -1]) /2
    else:
        median = X[int(len(X)/2)]
    return median
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    quartileArray = [0,0,0]
    arr = sorted(arr)
    quartileArray[1] = int(median(arr))
    if(len(arr) % 2 == 0):
         quartileArray[0] = int(median((arr[:int((len(arr)/2))])))
         quartileArray[2] = int(median((arr[int((len(arr)/2)):]))) 
    else:
         quartileArray[0] = int(median((arr[:int((len(arr)/2))])))
         quartileArray[2] = int(median((arr[int((len(arr)/2)+1):])))
         
    return quartileArray
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

#challenge from: https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

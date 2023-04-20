#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
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

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    final = []
    cont = 0
    for x in freqs:
        for y in range(x):
            final.append(values[cont])
        cont+=1
    z = quartiles(final)
    print(float(z[2] - z[0]))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

#challenge from: https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    
    z = 0
    for i in range(len(X)):
        z = z + X[i] * W[i]
        
    # Write your code here
    
    z = z/sum(W)
    print(round(z,1))
    return round(z,1)
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)

#challenge from: https://www.hackerrank.com/challenges/s10-weighted-mean/problem?h_r=next-challenge&h_v=zen
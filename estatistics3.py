#!/bin/python3
from math import sqrt


#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    z = 0

    media = sum(arr) / len(arr)
    for x in arr:
        z += pow(x - media,2)
    #z = sqrt(z)
    z = sqrt(z/len(arr))
    z = round(z,1)
    print(z)
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)

#challenge from: https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

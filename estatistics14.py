from math import *

def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def z(x,Mu,sigma):
    return (x-Mu) / sigma

mean_Mu = 205
standard_sigma = 15
numBoxes = 49

clt_mean_Mu = numBoxes * mean_Mu

clt_standard_sigma = sqrt(numBoxes) * standard_sigma


z_value = z(9800,clt_mean_Mu,clt_standard_sigma)
final = phi(z_value)
print(round(final,4))

#challenge from: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem?isFullScreen=true


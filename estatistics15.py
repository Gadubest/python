from math import *

def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def z(x,Mu,sigma):
    return (x-Mu) / sigma

mean_Mu = 2.4
standard_sigma = 2
students = 100

clt_mean_Mu = students * mean_Mu

clt_standard_sigma = sqrt(students) * standard_sigma

z_value = z(250,clt_mean_Mu,clt_standard_sigma)

final = phi(z_value)
print(round(final,4))

#challenge from: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2?isFullScreen=true
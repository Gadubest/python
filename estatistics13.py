from math import *

def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def z(x,Mu,sigma):
    return (x-Mu) / sigma

mean_Mu = 70
standard_sigma = 10
z_value = z(80,mean_Mu,standard_sigma)

first_case = 1 - phi(z_value)

z_value = z(60,mean_Mu,standard_sigma)

third_case = phi(z_value)

second_case = 1 - third_case
print(round(first_case * 100,2))
print(round(second_case * 100,2))
print(round(third_case * 100,2))

#challenge from: https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem?isFullScreen=true

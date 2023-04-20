import math

mean_Mu = 20
standard_sigma = 2
def z(x,Mu,sigma):
    return (x-Mu) / sigma
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
z_value = z(19.5,20,2)
less_Than = phi(z_value)

def z_Between(lower, higher):
    lower_value =phi(z(lower,mean_Mu,standard_sigma)) 
    higher_value =phi(z(higher,mean_Mu,standard_sigma)) 
    return higher_value - lower_value
Between = z_Between(20,22)
print(round(less_Than,3))
print(round(Between,3))

#challenge from: https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem?isFullScreen=true
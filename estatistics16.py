from math import * 

def z(x,Mu,sigma):
    return (x-Mu) / sigma


def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def standart_error(deviation,n):
    return deviation/sqrt(n)
mean_mu = 500
standart_sigma = 80
z_value = 1.96
numPeople = 100
resul_small = mean_mu - z_value * standart_error(standart_sigma,numPeople)
resul_big = mean_mu + z_value * standart_error(standart_sigma,numPeople)
print(resul_small)
print(resul_big)    

#challenge from: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem?isFullScreen=true
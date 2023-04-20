
k = 5
x = 2.5
e = 2.718281828459045235360287
def fatorial(x):
    if(x == 0):
        return 1
    for z in range(x-1,0,-1):
        x = x * z
    return x
def poissonDistribution(x,k):
    return ((x**k) * (e**(-x)) / fatorial(k))
print(round(poissonDistribution(x,k),3))

#challenge from: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?isFullScreen=true
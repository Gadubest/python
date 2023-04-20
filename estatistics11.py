def poisson_eX(Lambda):
    return Lambda + (Lambda ** 2)
def Cost(y,X):
    return y + 40 * X
x = poisson_eX(0.88)
x2 = poisson_eX(1.55)
A = Cost(160,x)
B = Cost(128,x2)
print(A)
print(B)

#challenge from: https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem?isFullScreen=true
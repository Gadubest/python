def fatorial(x):
    if(x == 0):
        return 1
    for z in range(x-1,0,-1):
        x = x * z
    return x

def binomial(n, x,p):
    try:
        np = fatorial(n) / ((fatorial(x) * (fatorial((n-x)))))
        resul = np * (p ** x) * ((1-p) ** (n-x))
        return resul
    except ZeroDivisionError:
        print(x, n)
        return 0
   
        
prob = 1.09 / 2.09
answer = 0
for boy in range(3,7):
    answer += binomial(6, boy, prob)
print(round(answer,3))

#challenge from: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem?isFullScreen=true



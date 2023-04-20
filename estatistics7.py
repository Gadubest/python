
def fatorial(x):
    if(x == 0):
        return 1
    for z in range(x-1,0,-1):
        x = x * z
    return x

def binomial(n, x,p):
    try:
        np = fatorial(n) / (fatorial(x) * (fatorial((n-x))))
        resul = np * (p ** x) * ((1 - p) ** (n - x))
        
        return resul
    except ZeroDivisionError:
        
        return 0

prob = 0.12
answer = 0
for piston in range(0,3):
    answer += binomial(10, piston, prob)
print(round(answer,3))
#print(f"the probability of no more than 2 rejects is {round(answer,3)}, or {round(answer,3) * 100}%")
answer = 0 
for piston in range(2,11):
    answer += binomial(10, piston, prob)
print(round(answer,3))
#print(f"the probability of at least 2 rejects is {round(answer,3)}, or {round(answer,3) * 100}%")

#challenge from: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem?isFullScreen=true


def geometric_Distribution(k,p):
    return round((1-p)**(k-1) * p,3)
resul = 0

for x in range(1,6):
    resul+= geometric_Distribution(x,1/3)
    
print(round(resul,3))

#challenge from: https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem?isFullScreen=true
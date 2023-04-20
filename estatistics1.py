from decimal import Decimal
import numpy as np
numbers = input('') #[64630 ,11735 ,14216, 99233, 14470 ,4978 ,73429, 38120, 51135, 67060]
X = numbers.split()
for i in range(len(X)):
    X[i] = int(X[i])
#mean = (sum(X) / (len(X) - 1))
mean = sum(X) / len(X)
X1 = sorted(X)
median = (X1[int(len(X)/2)]  + X1[int(len(X)/2) -1]) /2
mode =  {}

for number in X1:
    if not( mode.__contains__(number)):
        mode.update({number : 1})

    else:
        mode[number] = mode[number]+ 1

print(mean)
print(median)
greatest = max(mode,key= mode.get)
print(int(greatest))

#challenge from https://www.hackerrank.com/challenges/s10-basic-statistics/problem

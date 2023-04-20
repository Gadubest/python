from math import *
n = input()
input_data_X = (input()).split()
input_data_X = [float(k) for k in input_data_X]

input_data_Y = (input()).split()
input_data_Y = [float(k) for k in input_data_Y]

def rank(x):
    rank_value = []
    treated_x = list(dict.fromkeys(x))

    for k in x:
        less = 1
        for y in treated_x:
            if(k > y):
                less +=1
        rank_value.append(less)
    return rank_value

def mean(x):
    return sum(x) / len(x)

def standard_deviation(x):
    Mu_x = mean(x)
    deviations = ([(k - Mu_x)**2 for k in x])
    var = sum(deviations) / len(deviations)
    return sqrt(var)

def covariance(X,Y):
    Mu_X = mean(X)
    Mu_Y = mean(Y)

    suma = sum([(x - Mu_X) * (y - Mu_Y) for x,y in zip(X,Y)])
    return suma / (standard_deviation(X) * standard_deviation(Y) * len((X)))


X_rank = rank(input_data_X)
Y_rank = rank(input_data_Y)

print(round(covariance(X_rank,Y_rank),3))

#challenge from https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem?isFullScreen=true
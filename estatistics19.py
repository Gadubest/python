import math
import matplotlib.pyplot as plt


x = [95,85,80,70,60]
y = [85,95,70,65,70]
eta = 0.00001
plt.plot(x,y)
plt.show()


weigth = 0.25
bias = 0.5

predicted = [x[k] * weigth + bias for k in range(len(x))]


cost = sum([(predicted[k] - y[k]) ** 2 for k in range(len(y))])
print(f"initial cost = {cost}")

for j in range(100000):
    for k in range(len(x)):
        weigth-= 2* (predicted[k] - y[k]) * x[k] * eta
        
        bias-= 2* (predicted[k] - y[k])  * eta
    #print(f"epoch: {j}")
    #print(f"weigths: {start_weigth}")
    #print(f"bias: {start_bias}")
    predicted = [x[k] * weigth + bias for k in range(len(x))]
    cost = sum([(predicted[k] - y[k]) ** 2 for k in range(len(y))])
    #print(f"cost: {cost}")
print(f"final cost = {cost}")
print("resul: ", 80 * weigth + bias)
plt.plot([k * weigth + bias for k in x],y)
plt.show()



#challenge from: https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem?isFullScreen=true

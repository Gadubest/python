import numpy as np


input_shape = [int(k) for k in input().split(" ")]
values = []
#a= [input() for k in range(input_shape[1])]
for k in range(input_shape[1]):
     b = input().split(" ")
     for j in b:
         values.append(float(j))

X = []
resul = []

input_X_test_len= int(input())

input_test = []
for k in range(input_X_test_len):
    b = input().split(" ")
    for j in b:
        input_test.append(float(j))


input_test_X = []
#print(input_bias[0:2])
#print(input_bias[2:4])

for k in range(0,input_X_test_len * input_shape[0],input_shape[0]):
    
    input_test_X.append(input_test[k:input_shape[0]+k])

#fazer d acordo com o numero d linhas
for k in range(input_shape[1]):
    X.append(values[k * (input_shape[0] + 1):k * (input_shape[0] + 1) + input_shape[0]])
    

    resul.append(values[k * (input_shape[0] + 1) + input_shape[0]])






class network():
    def __init__(self, X, resul):
        self.X = X
        self.weights = np.random.randn(1,input_shape[0])
        self.bias = 0.1


    def calculate(self,eta):
        
        result = np.sum(np.array(self.X) * np.array(self.weights),axis=1)
        result = np.transpose([result])
        for k in range(len(result)):
            result[k] = result[k] + self.bias
        
        

        
        diff = (result - (np.array([(resul)]).T))**2
        ddiff = 2 * (result - (np.array([(resul)]).T))

        '''print("-----")
        print(result)
        print()
        print(np.array([(resul)]).T)
        print()
        print(ddiff)
        print("------")'''
        #print(np.average(diff))

        for k in range(input_shape[1]):
            for j in range(input_shape[0]):

                self.weights -= eta * ddiff[k] * X[k]


                self.bias -= eta * ddiff[k]
                

        return diff


    def results(self,test_X):
        
        
        result = []
        for k in range(len(test_X)):
            
            result.append(np.sum(test_X[k] * self.weights,axis=1) + self.bias)
        
        return np.array(result)


nn = network(X,resul)



for x in range(1000):
    nn.calculate(0.01)
felicidade = (nn.results(input_test_X))
for k in felicidade:
    print(k[0])
#[[90.65756353 46.39998277]]
#52.46153786
#0.18 0.89

#52.46153786 + 90.65756353 * 0.18 + 46.39998277 * 0.89

#52.46153786 + 90.65756353 * 0.49 + 46.39998277 * 0.18
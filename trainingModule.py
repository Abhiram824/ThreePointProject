import numpy as np

def predict(listx, listy, weights, bias):
    predictions = np.dot(listx, weights)
    predictions = (i + bias for i in predictions)
    return predictions

def cost(predictedVals, realVals):
    cost = 0
    length = len(predictedVals)
    for i in range(length):
        cost += (realVals - predictedVals) ** 2
    return cost/length


#def gradient(listx, listy, weights, bias, learningRate):

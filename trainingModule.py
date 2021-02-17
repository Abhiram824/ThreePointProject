import numpy as np

# functions are for single variable linear regression
def normalize(max, min, val):
    return(val-min)/(max-min)

def predict(listx, listy, weight, bias):
    predictions = np.dot(listx, weight)
    predictions = (i + bias for i in predictions)
    return predictions

def cost(predictedVals, realVals):
    cost = 0
    length = len(predictedVals)
    for i in range(length):
        cost += (realVals[i] - predictedVals[i]) ** 2
    return cost/length


def gradient(listx, listy, weight, bias):
    #calculating both bias and weight gradient to minimize iterations
    weightGradient = 0
    bGradient = 0
    length = len(listy)
    predictions = predict(listx, listy, weight, bias)
    for i in range(length):
        error = predictions[i] - listy[i]
        weightGradient += 2 * error * listx[i]
        bGradient += 2 * error
    weightGradient /= length
    bGradient /= length

    return weightGradient, bGradient

def updateVals(weight, bias, weightGradient, bGradient, learningRate):
    weight += weightGradient * learningRate
    bias += bGradient * learningRate
    return weight, bias

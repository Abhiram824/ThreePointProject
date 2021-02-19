import numpy as np

# functions are for single variable linear regression
# is returning multiple values best practice?
#Using linear regression for r^2 or should I switch to logistic?
def normalize(max, min, val):
    return(val-min)/(max-min)

def predict(listx, weight, bias):
    predictions = [(i * weight) + bias for i in listx]
    return predictions

def cost(predictedVals, realVals):
    cost = 0
    length = len(predictedVals)
    for i in range(length):
        cost += ((realVals[i] - predictedVals[i]) ** 2)
    return cost/length


def gradient(listx, listy, weight, bias):
    #calculating both bias and weight gradient to minimize iterations
    weightGradient = 0
    bGradient = 0
    length = len(listy)
    predictions = predict(listx, weight, bias)

    for i in range(length):
        error = predictions[i] - listy[i]
        weightGradient += 2 * error * listx[i]
        bGradient += 2 * error
    weightGradient /= length
    bGradient /= length

    return weightGradient, bGradient

def train(listx, listy, weight, bias, learningRate, epochs):
    for i in range(epochs):
        weightGradient, bGradient = gradient(listx, listy, weight, bias)
        weight -= weightGradient * learningRate
        bias -= bGradient * learningRate
    return weight, bias

def divide(inputVals, outputVals, ratio):
    #not sure how to return less because python pass by reference is weird
    length = len(inputVals)
    divide = int (ratio * length)

    testInputs = [inputVals[i] for i in range(divide, length, 1)]
    testOutputs = [outputVals[i] for i in range(divide, length, 1)]

    inputVals = [inputVals[i] for i in range(divide)]
    outputVals = [outputVals[i] for i in range(divide)]
    

    return inputVals, outputVals, testInputs, testOutputs

def list_average(list_of_vals):
    average = 0
    length = len(list_of_vals)
    for i in range(length):
        average += list_of_vals[i]
    return average/length



            

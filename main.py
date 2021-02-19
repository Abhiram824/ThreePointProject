import dataScrape as ds
import trainingModule as tm
import numpy as np
import matplotlib.pyplot as plt

#constants
PLAYERWEBSITE = "https://www.basketball-reference.com/players/"
GENERALWEBSITE = "https://www.basketball-reference.com/"
FREETHROWINDEX = 1
THREEPTINDEX = 0
ALPHABET = ["a/", "b/", "c/", "d/", "e/", "f/", "g/", "h/", "i/", "j", "k/", "l/", "m/", "n/", "o/", "p/", "q/", "r/", "s/", "t/", "u/", "v/", "w/", "x/", "y/", "z/"]
EXCLUDEDPOS = "C"
MINYEARSPLAYED = 2
MINYEAR = 2008
FREETHROWATTRIBUTE = "ft_pct"
THREEPTATTRIBUTE = "fg3_pct"
INITIALIZER = 0
LEARNINGRATE = .025
EPOCHS = 500
DIVIDE = 0.8
COSTMULTIPLIER = 1000

list_of_links = []
length = len(ALPHABET)
for i in range(length):
    list_of_links.append(ds.filter_players(PLAYERWEBSITE + ALPHABET[i] , MINYEAR, EXCLUDEDPOS, MINYEARSPLAYED))
    
training_input_vals = []
training_output_vals = []

for links in list_of_links:
    for link in links:
        training_input_vals.append(ds.extract_stats(GENERALWEBSITE + link, [THREEPTATTRIBUTE, FREETHROWATTRIBUTE])[FREETHROWINDEX])
        training_output_vals.append(ds.extract_stats(GENERALWEBSITE + link, [THREEPTATTRIBUTE, FREETHROWATTRIBUTE])[THREEPTINDEX])

training_input_vals, training_output_vals, test_inputs, test_outputs = tm.divide(training_input_vals, training_output_vals, DIVIDE)

weight = INITIALIZER
bias = INITIALIZER

weight, bias = tm.train(training_input_vals, training_output_vals, weight, bias, LEARNINGRATE, EPOCHS)
predicted_vals = tm.predict(test_inputs, weight, bias)
cost = tm.cost(predicted_vals, test_outputs)


r_squared = tm.r_squared(predicted_vals, test_outputs)

print(predicted_vals, test_outputs, weight, bias)
print(r_squared, COSTMULTIPLIER * cost)


plt.plot(predicted_vals, predicted_vals)
plt.scatter(test_inputs, test_outputs)

plt.show()


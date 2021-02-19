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
    
total_input_vals = []
total_output_vals = []
stats = [THREEPTATTRIBUTE, FREETHROWATTRIBUTE]
stats_length = len(stats)

for links in list_of_links:
    for link in links:
        extracted_stats = ds.extract_stats(GENERALWEBSITE + link, stats)
        if len(extracted_stats) == stats_length:
            total_input_vals.append(extracted_stats[FREETHROWINDEX])
            total_output_vals.append(extracted_stats[THREEPTINDEX])

training_input_vals, training_output_vals, test_inputs, test_outputs = tm.divide(total_input_vals, total_output_vals, DIVIDE)

weight = INITIALIZER
bias = INITIALIZER

weight, bias = tm.train(training_input_vals, training_output_vals, weight, bias, LEARNINGRATE, EPOCHS)
predicted_vals = tm.predict(test_inputs, weight, bias)
cost = tm.cost(predicted_vals, test_outputs)


r_squared = tm.r_squared(total_input_vals, total_output_vals)

print(predicted_vals, test_outputs, weight, bias)
print(r_squared, COSTMULTIPLIER * cost)
print("very disappointing r^2 value as it is rather low, showing a weak correlation. I will look into results again, but it looks like free throw percentage is not the best indicator of three point percentage")
print("the graph also shows a lackluster correlation.")
plt.plot(test_inputs, predicted_vals)
plt.scatter(test_inputs, test_outputs)

plt.show()
#results show an r^2 of about.28 which show a low correlation, but the plot shows otherwise, so I will double check my results
#looks like my gradient descent for linear regression was not perfect. May have to switch algorithms


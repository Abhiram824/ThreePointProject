import dataScrape as ds
import trainingModule as tm
import numpy as np
import matplotlib.pyplot as plt


PLAYERWEBSITE = "https://www.basketball-reference.com/players/"
GENERALWEBSITE = "https://www.basketball-reference.com/"
FREETHROWINDEX = 1
THREEPTINDEX = 0
ALPHABET = ["a/", "b/", "c/", "d/", "e/", "f/", "g/", "h/", "i/", "j", "k/", "l/", "m/", "n/", "o/", "p/", "q/", "r/", "s/", "t/", "u/", "v/", "w/", "x/", "y/", "z/"]
list_of_links = []
length = 0
for i in range(3):
    list_of_links.append(ds.filter_players(PLAYERWEBSITE + ALPHABET[i] , 2008, "C", 2))
    
training_input_vals = []
training_output_vals = []

for links in list_of_links:
    for link in links:
        training_input_vals.append(ds.extract_stats(GENERALWEBSITE + link, ["fg3_pct", "ft_pct"])[FREETHROWINDEX])
        training_output_vals.append(ds.extract_stats(GENERALWEBSITE + link, ["fg3_pct", "ft_pct"])[THREEPTINDEX])

training_input_vals, training_output_vals, test_inputs, test_outputs = tm.divide(training_input_vals, training_output_vals, 0.8)

weight = 0
bias = 0

weight, bias = tm.train(training_input_vals, training_output_vals, weight, bias, .025, 500)
predicted_vals = tm.predict(test_inputs, weight, bias)
cost = tm.cost(predicted_vals, test_outputs)


correlation_matrix = np.corrcoef(predicted_vals, test_outputs)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(predicted_vals, test_outputs, weight, bias)
print(r_squared, 1000 * cost)


plt.plot(predicted_vals, predicted_vals)
plt.scatter(test_inputs, test_outputs)

plt.show()


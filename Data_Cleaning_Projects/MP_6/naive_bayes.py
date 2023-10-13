import csv
import fileinput
from math import log2, log, log10
data = fileinput.input(files ="sample_6.csv")
#data = fileinput.input()
rows = []
sample = [row for row in csv.reader(data)]
print(sample)
test_dict = {}
training_dict = {}
for row in sample:
    if row == sample[0]:
        reference_row = row
    else:
        if row[-1] == '-1':
            if row[0] in test_dict:
                duplicate_number_test = len([key for key in test_dict if row[0] in key]) + 1
                test_dict[row[0], duplicate_number_test] = row[1::]
            else:
                test_dict[row[0]] = row[1::]
        else:
            training_dict[row[0]] = row[1::]

#print(training_dict)
#print(test_dict)

#Get total values for each class by interating through the test dict and retrieving last item in each list and summing occurences
def get_totals_for_each_class(training, test):
    total_class_values = {}
    probs_per_attribute_per_class = {}
    for i in range(1, 8):
        total_class_values[i] = 0
    for training_dict_values in training_dict.values():
        total_class_values[int(training_dict_values[-1])] += 1
    return(total_class_values)

def get_prior_class_probability_with_laplacian(training_set_length, class_total_values):
    p_c = {}
    for classs in class_total_values:
        p_c[classs] = (class_total_values[classs] + .1)/(training_set_length + (.1 * 16))
    return(p_c)

def get_prob_attribute_per_class(test_dict, total_class_values, training_dict):
    probability_for_each_attribute_per_class = {}
    test_dict_values = [item for item in test_dict if item != '-1']
    animal_list = []
    for classs in total_class_values:
        probability_for_each_attribute_per_class[classs] = []
        for i in range(len(test_dict_values)):
            animal_list = [animal for animal in training_dict.values() if animal[i] == test_dict_values[i] and animal[-1] == str(classs)]
            number_of_samples = len(animal_list) + .1
            if i == 13:
                feature_attribute = .6
            else:
                feature_attribute = .2
            probability_for_each_attribute_per_class[classs].append(number_of_samples/(total_class_values[classs] + feature_attribute))
    #print(probability_for_each_attribute_per_class)
    return(probability_for_each_attribute_per_class)

def add_probabilities(class_att_probabilities):
    probability_sum = {}
    for animal_class in class_att_probabilities:
        probability_sum[animal_class] = sum(log(p) for p in class_att_probabilities[animal_class])
    return(probability_sum)

def multiply_by_prior_class(probability_sums, prior_classes):
    final_probabilities = {}
    for i in range(1, 8):
        final_probabilities[i] = probability_sums[i] #* prior_classes[i]
    return(final_probabilities)
        

class_dict = get_totals_for_each_class(training_dict, test_dict)
#print(class_dict)

class_prior_probability = get_prior_class_probability_with_laplacian(len(training_dict), class_dict)
#print(class_prior_probability)

for test in test_dict.values():
    attribute_probabilities = get_prob_attribute_per_class(test, class_dict, training_dict)
    #print(attribute_probabilities)
    combined_probabilities = add_probabilities(attribute_probabilities)
    #print(combined_probabilities)
    final_probabilities = multiply_by_prior_class(combined_probabilities, class_prior_probability)
    #print(final_probabilities)
    highest_probability = list(key for key in final_probabilities.keys() if final_probabilities[key] == max(final_probabilities.values()))[0]
    print(highest_probability)


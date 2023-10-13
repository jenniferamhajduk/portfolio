import fileinput
from math import log10
from math import sqrt
from itertools import combinations
#data = fileinput.input()
data = fileinput.input(files ="sample_input")

def get_jaccard_similarity(label_length, cluster_labels, predicted_labels):
    tp = 0
    fp = 0
    fn = 0
    paired_values = list(zip(cluster_labels, predicted_labels))
    for i in range(len(paired_values)):
        for j in range(i + 1, len(paired_values)):
            if paired_values[i][0] == paired_values[j][0] and paired_values[i][1] == paired_values[j][1]:
                tp += 1
            if paired_values[i][0] == paired_values[j][0] and paired_values[i][1] != paired_values[j][1]:
                fn += 1
            if paired_values[i][0] != paired_values[j][0] and paired_values[i][1] == paired_values[j][1]:
                fp += 1
    # for i, j in combinations(range(label_length), 2):
    #     cluster_label_in_correct_cluster = cluster_labels[i] == predicted_labels[j]
    #     predicted_label_has_correct_clusters = predicted_labels[i] == cluster_labels[j]
    #     if cluster_label_in_correct_cluster and predicted_label_has_correct_clusters:
    #         tp += 1
    #     elif cluster_label_in_correct_cluster and not predicted_label_has_correct_clusters:
    #         fp += 1
    #     elif not cluster_label_in_correct_cluster and predicted_label_has_correct_clusters:
    #         fn += 1
    return "{:.3f}".format((tp/(tp + fp + fn)))


def get_nmi_similarity(cluster_labels, predicted_labels):
    paired_values = list(zip(cluster_labels, predicted_labels))
    total_values = len(paired_values)

    #Get unique values to prevent double counting in entropy calculations
    unique_cluster_labels = set()
    unique_prediction_labels = set()
    unique_sets = set()
    for cluster_label in cluster_labels:
        unique_cluster_labels.add(cluster_label)
        for predicted_label in predicted_labels:
            unique_prediction_labels.add(predicted_label)
            for value in paired_values:
                unique_sets.add(value)
    #Get Entropy of cluster labels
    cluster_entropy = 0
    for cluster_label in unique_cluster_labels:
        cluster_entropy += -(cluster_labels.count(cluster_label)/total_values) * log10((cluster_labels.count(cluster_label)/total_values))

    #Get Entropy of pedicted labels
    predicted_entropy = 0
    for predicted_label in unique_prediction_labels:
        predicted_entropy += -(predicted_labels.count(predicted_label)/total_values) * log10((predicted_labels.count(predicted_label)/total_values))


    #Get mutual information       
    mutual_information = 0
    for unique_set in unique_sets:
        ci = cluster_labels.count(unique_set[0])/total_values
        pi = predicted_labels.count(unique_set[1])/total_values
        mutual_information += (paired_values.count(unique_set)/total_values) * log10((paired_values.count(unique_set)/total_values)/(pi * ci))

    #Get normalized mutual information
    nmi = mutual_information/sqrt((predicted_entropy * cluster_entropy))
    return "{:.3f}".format(nmi)      

cluster_labels = []
predicted_labels = []

#format data
for line in data:
    split_line = list(map(int, line.strip().split()))
    cluster_labels.append(split_line[0])
    predicted_labels.append(split_line[1])

label_length = len(cluster_labels)
jaccard = get_jaccard_similarity(label_length, cluster_labels, predicted_labels)
nmi = get_nmi_similarity(cluster_labels, predicted_labels)
print(str(nmi) + " " + str(jaccard))

import fileinput
import math
from operator import itemgetter
data_points = []
data = fileinput.input()
#data = fileinput.input(files ="sample_input_minimum")
#data = fileinput.input(files ="sample_input_maximum")
#data = fileinput.input(files ="sample_input_average")

#Funtion that returns the tuple of the cluster item index, neighbor item index, and the distance
def get_euclidean_distance(m_function, cluster_dictionary, indices_a, indices_b):
    if type(indices_a) is tuple and type(indices_b) is tuple:
        distance_list = []
        for i in indices_a:
            for j in indices_b:
                distance_list.append(math.sqrt(sum([(a - b) ** 2 for a, b in zip(cluster_dictionary[i], cluster_dictionary[j])])))
        distance = m_function(distance_list)
    elif type(indices_a) is not tuple and type(indices_b) is not tuple:
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(cluster_dictionary[indices_a], cluster_dictionary[indices_b])]))
    else:
        if type(indices_a) is tuple:
            cluster_indices = indices_a
            index = indices_b
        else:
            cluster_indices = indices_b
            index = indices_a
        distance_list = []
        for i in cluster_indices:
            distance_list.append(math.sqrt(sum([(a - b) ** 2 for a, b in zip(cluster_dictionary[i], cluster_dictionary[index])])))
        distance = m_function(distance_list)
    return distance

#Main
#Initialize cluster values
for line in data:
    if data.isfirstline():
        n, k, m = line.split()
    else:
        data_points.append(tuple(map(float, line.strip().split())))

clusters = []
for i in range(int(n)):
    clusters.append(data_points[i])

def mean(l):
    return sum(l)/len(l)

m_func_dict = {0: min, 1: max, 2: mean}
m_function = m_func_dict[int(m)]
cluster_indices = list(range(len(clusters)))

#Start the loop
while len(cluster_indices) > int(k):
    distance_matrix = {}
    i_counter = 0
    for i in cluster_indices:
        j_counter = 0
        for j in cluster_indices:
            if (i, j) not in distance_matrix and i_counter < j_counter:
                distance_matrix[(i, j)] = get_euclidean_distance(m_function, data_points, i, j)
            j_counter += 1
        i_counter += 1
    
    #Update Clusters
    smallest_distance_indices = min(distance_matrix.items(), key = itemgetter(1))[0]
    i, j = smallest_distance_indices
    if type(i) is tuple and type(j) is tuple:
        new_cluster = i + j
    elif type(i) is not tuple and type(j) is not tuple:
        new_cluster = (i, j)
    else:
        if type(i) is tuple:
            cluster = i
            single = j
        else:
            cluster = j
            single = i
        new_cluster = cluster + (single, )

    cluster_indices.remove(i)
    cluster_indices.remove(j)
    cluster_indices.append(new_cluster)

cluster_labels = {}
cluster_count = 0
for cluster in cluster_indices:
    cluster_labels[cluster] = cluster_count
    cluster_count += 1

for i in range(len(data_points)):
    for cluster in cluster_indices:
        if type(cluster) is int:
            if i == cluster:
                print(cluster_labels[cluster])
                break
        elif i in cluster:
            print(cluster_labels[cluster])
            break

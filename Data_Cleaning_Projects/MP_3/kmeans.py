import math
import numpy as np
from random import randint

places = open("places.txt", "r").readlines()
clusters_txt = open("clusters.txt", "w")
clusters = {}
centroids = {}
k = 3

#Prep Data
data = [tuple(map(float, point.strip().split(','))) for point in places]

def getRandomCentroid(p):
    random_value = randint(0, len(places))
    return random_value

#Get Euclidean distance
def getEuclideanDistance(point_a, point_b):
    distance = np.linalg.norm(point_a - point_b)
    return distance

#Initialize centroids and empty cluster dictionary
for i in range(k):
    centroids[i] = tuple(map(float, places[getRandomCentroid(places)].strip().split(',')))
    clusters[i] = []
print("The points are: " + str(centroids))

#Input Initial Centroid Values

#Get Distances
index = 0
for point in data:
    distances = {}
    key = []
    for i in range(k):
        distances[i] = getEuclideanDistance(np.array(point), np.array(centroids[i]))
    min_distance = min(distances.values())
    key_value = [key for key in distances if distances[key] == min_distance]
    clusters[key_value[0]].append(min_distance)
    clusters_txt.write( str(index) + " " + str(key_value) + '\n')
    index += 1


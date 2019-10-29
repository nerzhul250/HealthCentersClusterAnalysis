# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:36:25 2019

@author: asus
"""

import os.path

my_path=os.path.abspath(os.path.dirname(__file__))

#numpy
import numpy as np

#sklearn
from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity


#pyclustering
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.kmeans import kmeans
from pyclustering.utils import read_sample
#silhouette to evaluate clusterization quality
from pyclustering.cluster.silhouette import silhouette

import dataScienceUtils as ut

#define basic info
path=os.path.join(my_path,'rawDataToFormattedData\\PorCentrosDeSalud\\formattedData.txt')


# load list of points for cluster analysis
sample = read_sample(path)
number_of_data_points=len(sample)
#preprocessing
sample=preprocessing.normalize(np.asarray(sample))

base_individuals=100
number_of_keis=1
number_of_clusters_k=9
#Initial poblation
def get_random_individual(sample, k):
    return kmeans_plusplus_initializer(sample,k, kmeans_plusplus_initializer.FARTHEST_CENTER_CANDIDATE).initialize()

def compute_score(individual,sample):
    kmeans_instance = kmeans(sample,individual)
    kmeans_instance.process()
    clusters = kmeans_instance.get_clusters()
    dirtyscore = silhouette(sample, clusters).process().get_score()
    score=[x if str(x)!='nan' else 0 for x in dirtyscore]
    return np.mean(np.asarray(score))

poblation=[get_random_individual(sample,k)  for i in range(base_individuals) for k in range(number_of_clusters_k,number_of_keis+number_of_clusters_k)]
poblation=[(x,compute_score(x,sample)) for x in poblation]

def custom_sort(individual):
    return -individual[1]

poblation.sort(key=custom_sort)

lucky_individuals=10

def cross(individual1,individual2):
    minimum_length=min(len(individual1[0]),len(individual2[0]))
    maximum_length=max(len(individual1[0]),len(individual2[0]))
    new_individual=[]
    for i in range(minimum_length):
        new_individual.append((individual1[0][i]+individual2[0][i])/2)
    for i in range(minimum_length+1,int((minimum_length+maximum_length)/2)):
        if len(individual1[0])==maximum_length:
            new_individual.append(individual1[0][i])
        else:
            new_individual.append(individual2[0][i])
    return (new_individual,compute_score(new_individual,sample))            

for t in range(30):
    print(t)
    ofspring=[]
    for i,x in enumerate(poblation):
        for j,y in enumerate(poblation):
            if i<j and i<lucky_individuals and j<lucky_individuals:
                ofspring.append(cross(x,y))
    for of in ofspring:
        poblation.append(of)
    poblation.sort(key=custom_sort)
    poblation=poblation[:base_individuals]

print("")
#sillhouete score
print(len(poblation[0][0]))

kmeans_instance = kmeans(sample,poblation[0][0])
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()
print(poblation[0][1])
for clusteri in clusters:
    print(clusteri)
    

cosine_similarities_matrix=cosine_similarity(sample)

print("")
#Homogeneidad interna total y heterogeneidad externa total
HIT,HET=ut.get_HIT_HET(clusters,cosine_similarities_matrix)


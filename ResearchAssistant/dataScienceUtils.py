# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 05:47:14 2019

@author: asus
"""

#numpy
import numpy as np

#MATPLOTLIB
#%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



def get_distance_matrix(sample):
    number_of_data_points=len(sample)
    return [[np.linalg.norm(sample[j]-sample[i]) for i in range(number_of_data_points)] for j in range(number_of_data_points)]
    

def initial_medoids_paper_method(sample,k,distances):    
    number_of_data_points=len(sample)
    #construct indices that will be used for the initial medoids
    indices=[index for index in range(number_of_data_points)]
    
    #define function for computing the clustarization of each point defined in the paper
    def calc(index):
        result=0
        for i in range(number_of_data_points):
            intermedium=0
            for l in range(number_of_data_points):
                intermedium=intermedium+distances[i][l]
            result=result+(distances[i][index]/intermedium)
        return result

    #compute vjs
    vjs=[calc(i) for i in range(number_of_data_points)]

    #define comparator function to sort the indices
    def cmp(elem):
        return vjs[elem]
    
    #sort
    indices.sort(key=cmp)
    
    return indices[:k]

def plot_clusters(clusters,samples_embedded):
    number_of_data_points=len(samples_embedded)
    exes=[samples_embedded[x][0] for x in range(number_of_data_points)]
    eyes=[samples_embedded[x][1] for x in range(number_of_data_points)]
    for cluster in clusters:
        cluster_color=np.random.choice(range(256),size=3)
        my_color='#%02x%02x%02x' % tuple(cluster_color)
        for x in cluster:
            plt.scatter(exes[x],eyes[x],color=str(my_color))
            plt.annotate(x,(exes[x],eyes[x]))
    plt.show()
    
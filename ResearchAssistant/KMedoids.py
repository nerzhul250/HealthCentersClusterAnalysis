# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:34:54 2019

@author: asus
"""
import os.path

my_path=os.path.abspath(os.path.dirname(__file__))

#numpy
import numpy as np

#sklearn
from sklearn.manifold import TSNE
from sklearn import preprocessing
from sklearn.decomposition import TruncatedSVD

#pyclustering
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.utils import read_sample
#silhouette to evaluate clusterization quality
from pyclustering.cluster.silhouette import silhouette

#MATPLOTLIB
#%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

import dataScienceUtils as ut

#define basic info
path=os.path.join(my_path,'rawDataToFormattedData\\PorCentrosDeSalud\\formattedData.txt')

# load list of points for cluster analysis
sample = read_sample(path)
number_of_data_points=len(sample)
#preprocessing
sample=preprocessing.normalize(np.asarray(sample))
#get distance matrix
distances=ut.get_distance_matrix(sample)

# set k initial medoids
k=4

print("Numero de Clusters:")
print(k)
print("\n")


print("PERFORMING KMEDOIDS\n")


#get initial medoids
initial_medoids = ut.initial_medoids_paper_method(sample,k,distances)

# create instance of K-Medoids algorithm
kmedoids_instance = kmedoids(sample, initial_medoids)

# run cluster analysis and obtain results
kmedoids_instance.process();
clusters = kmedoids_instance.get_clusters()

# show clusters
for clusteri in clusters:
    print(clusteri)
print("\n")

# Calculate Silhouette score
dirtyscore = silhouette(sample, clusters).process().get_score()
score=[x for x in dirtyscore if str(x)!='nan']

print("score promedio de silhoette")
print(np.mean(np.asarray(score)))
print("\n")

#computing minimum distance in data
minimo=[np.asarray([distances[i][j] for j in range(number_of_data_points) if distances[i][j]!=0]) for i in range(number_of_data_points)]
minimo=[np.min(x) for x in minimo]
minimo=np.asarray(minimo)
minimo=np.min(minimo)
print("minima distancia")
print(minimo)
indices=[(i,j) for i in range(22) for j in range(22) if distances[i][j]==minimo and i<j]
print("indices")
print(indices)
print("\n")

#computing maximum distance in data
maximo=[np.asarray([distances[i][j] for j in range(number_of_data_points) if distances[i][j]!=0]) for i in range(number_of_data_points)]
maximo=[np.max(x) for x in maximo]
maximo=np.asarray(maximo)
maximo=np.max(maximo)
print("maxima distancia")
print(maximo)
indices=[(i,j) for i in range(22) for j in range(22) if distances[i][j]==maximo and i<j]
print("indices")
print(indices)
print("\n")

#sklearn, T-SNE dimensionality reduction
samples_embedded=TSNE(n_components=2).fit_transform(sample)
print("plotting using t-sne dimensionality reduction")
ut.plot_clusters(clusters,samples_embedded)


#sklearn, SVD dimensionality reduction
print("Plotting ussing SVD dimensionality reduction")
svd = TruncatedSVD()
samples_embedded=svd.fit_transform(sample)
ut.plot_clusters(clusters,samples_embedded)
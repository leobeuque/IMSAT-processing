import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image
from pathlib import Path
import sys


def initRandom(k,data,seed=1):
    mm = data.mean()
    std = data.std()
    np.random.seed(seed)
    cent = np.random.normal(mm,std,(k,data.shape[1]))
    return cent

def myDistance(ar,centroid):
    ar = ar.copy()
    c = centroid.copy()
    diff = (ar - c[:,np.newaxis])**2
    distance = (np.sum(diff,axis=2))**0.5
    return distance.T

def myKmeans(data,k,n=10,seed=1):
    data = data.copy()
    centr = initRandom(k,data,seed)
    centInit = centr.copy()

    with np.errstate(divide='ignore', invalid='ignore'):

        for it in range(n):
            distance = myDistance(data,centr)
            idx = np.argmin(distance,axis=1)
            labels = idx + 1

            centOld = centr.copy()
            centr = [data[idx==i].mean(axis=0) for i in np.unique(idx)]
            centr = np.array(centr)

    return centr,labels,centInit


def myScat(data,centroids=None,labels=None,size=5):
    xy = data.copy()

    f = plt.figure(figsize=(size,size))
    # plot raw data (black)
    if centroids is None:
        plt.scatter(xy[:,0], xy[:,1], marker='.', s=7, color = 'k')

    # plot raw data (black) and red centroids
    elif centroids is not None and labels is None:
        plt.scatter(xy[:, 0], xy[:, 1], marker='.', s=7, color = 'k')
        plt.plot(centroids[:,0],centroids[:,1],'*',c='r',markersize=10)

    # plot data as colored clusters and red centroids
    elif centroids is not None and labels is not None:
        np.random.seed(444999)
        colors = np.random.rand(k,3)

        lab = np.unique(labels)
        for i,l in enumerate(lab):
            idx = labels == l
            c = colors[i]
            plt.scatter(xy[idx,0], xy[idx,1], marker='.', s=7, color = c);
        plt.plot(centroids[:,0],centroids[:,1],'*',c='r',markersize=10)

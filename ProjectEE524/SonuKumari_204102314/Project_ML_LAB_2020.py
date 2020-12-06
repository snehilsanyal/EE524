#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.datasets import load_boston
from matplotlib import cm  # color map
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import seaborn as sns 
from sklearn import metrics
from scipy.linalg import eigh


# ## 1) PCA on Boston Housing Dataset

# ## 1.a) Load The Dataset

# In[141]:


boston_dataset = load_boston()
csvfile = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
y = boston_dataset.target
csvfile.head()


# ## 1.b) Standardizing The Dataset

# In[142]:


# fitting dataset into standardscaler
snd = StandardScaler().fit_transform(csvfile)


# ## 1.c) Covarience 

# In[143]:


# covarience matrix cov = X.T*X
cov = np.matmul(snd.T,snd)
# finding top two eigen values and corresponding eigen vectors using scipy.linalg by importing eigh
values , vectors = eigh(cov,eigvals=(11,12))
# for matrix multiplication change shape of vectors from 13*2 to 2*13
vectors = vectors.T


# ## 1.d) Principal Component

# In[144]:


# matrix multiplication of vectors(2*13) to snd transpose size (13*506)
project= np.matmul(vectors,snd.T)
# appending target to projected new 
new = np.vstack((project,y)).T
# creating new dataframe
df = pd.DataFrame(data=new,columns=("1 principal","2 principal","target"))
print(df)


# ## 1.e) Visualization

# In[145]:


# seaborn plot of new projected dataframe
sns.FacetGrid(df,hue = "target",height=6).map(plt.scatter,'1 principal','2 principal')
plt.show()


# ## 2) KNN On Boston Housing Dataset

# ## 2.a) Load The Dataset

# In[155]:


boston_data = load_boston()
df = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
df.head()


# ## 2.b) Root Mean Square 

# In[147]:


def compute_rmse(predictions, yvalues):
    error_sq = (predictions - yvalues)**2
    error_sq = error_sq.sum()
    rmse = np.sqrt(error_sq/float(len(predictions)))
    return rmse


# In[148]:


def distance(x1, x2):
    sqr = (x1-x2)**2
    dista = sqr.sum(axis = 1)
    return np.array(dista)


# ## 2.c) Spliting dataset

# In[156]:


np.random.seed(seed=13579)
# int(len(bdata.target)*0.66)

# Function to randomly split the data into test and train
def random_split(data, target, per_train):
    data = np.insert(data, data.shape[1],target, axis = 1)
    np.random.shuffle(data)
    train = data[0:int(per_train*len(target)),:]
    test = data[int(per_train*len(target)):len(target),:]
    return train, test, data

# Create train, test and entire dataset using the random_split function
bdata_train, bdata_test, data = random_split(boston_data.data, boston_data.target, 0.66)


# ## 2.d) Normalization

# In[157]:


# min max normalization
def normalize(raw_data, mn):
    normalized_data = (raw_data-mn)/float(np.max(raw_data)-np.min(raw_data))
    return normalized_data

# Function we will use in our analysis
def normalize2(raw_data):
    normalized_data = (raw_data-np.min(raw_data))/float(np.max(raw_data)-np.min(raw_data))
    return normalized_data


# In[158]:


# Normalizing entire dataset for future use
norm_data = np.vstack((normalize2(bdata.data[:,0]), normalize2(bdata.data[:,1]), normalize2(bdata.data[:,2]),
                     normalize2(bdata.data[:,3]), normalize2(bdata.data[:,4]), normalize2(bdata.data[:,5]), 
                     normalize2(bdata.data[:,6]), normalize2(bdata.data[:,7]), normalize2(bdata.data[:,8]),
                     normalize2(bdata.data[:,9]), normalize2(bdata.data[:,10]), normalize2(bdata.data[:,11]),
                     normalize2(bdata.data[:,12]), (bdata.target))).T


# ## 2.e) Neighbour

# In[175]:


def neighbor(train, test, col_num, target, k=1):
    final = []
    for i in range(len(test)):
        dist = distance(train[:,col_num], test[i,col_num])        
        dist = dist[:, np.newaxis]
        dist2 = np.append(dist, train[:,target],1)
        
        sortd = dist2[np.argsort(dist2[:,0]),:][0]  
        final.append(sortd)
    
    neigh = np.array(final)
    final = np.append(neigh, test[:, target], axis = 1)
    rmse = compute_rmse(final[:,1], final[:,2])
    return rmse
print("neighbours are ",neighbor(bdata_train, bdata_test,[0,5],[13]))
# Calulating the normalized values of test and train data
test = np.vstack((normalize2(bdata_test[:,0]),normalize2(bdata_test[:,5]),(bdata_test[:,13]))).T
train = np.vstack((normalize2(bdata_train[:,0]),normalize2(bdata_train[:,5]),(bdata_train[:,13]))).T
z = neighbor(train, test, [0,1], [2])
print( ' input based on nearest neighborsn algorithm: ', z)


# In[176]:


test= np.vstack((normalize2(bdata_test[:,12]), normalize2(bdata_test[:,0]),
                  normalize2(bdata_test[:,5]),normalize2(bdata_test[:,6]),normalize2(bdata_test[:,9]),
                  (bdata_test[:,13]))).T
train= np.vstack((normalize2(bdata_train[:,12]),normalize2(bdata_train[:,0]),
                    normalize2(bdata_train[:,5]),normalize2(bdata_train[:,6]),normalize2(bdata_train[:,9]),
                    (bdata_train[:,13]))).T
print( neighbor(train, test, [0,1,2,3,4], [5], 2))
print( neighbor(train, test, [0,1,2,3,4], [4], 3))


# ## 2.f) KNN

# In[181]:


def knn(train, test, col_num, target, K):
    final1 = []
    for j in range(len(test)):
        dist = distance(train[:,col_num], test[j,col_num])        
        dist = dist[:, np.newaxis]
        dist2 = np.append(dist, train[:,target],1)
        sortd = dist2[np.argsort(dist2[:,0]),:]
        final1.append(np.mean(sortd[0:K], axis = 0))
    f_arr = np.array(final1)
    final = np.append(f_arr, test[:,target],1)
    rmse = compute_rmse(final[:,1], final[:,2])
    return rmse
print("knn for testing dataset ", knn(bdata_train, bdata_test, [0,5], [13], 3))
 


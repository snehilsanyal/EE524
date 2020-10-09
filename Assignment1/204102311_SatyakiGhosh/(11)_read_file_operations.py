import numpy as np
import csv

path='/home/satyaki/Desktop/IIT GUWAHATI/Courses/Machine Learning Laboratory/Assignments/Assignment 1'

#METHOD 1
points=np.loadtxt(open(path+'/10_points.csv', "rb"), delimiter=",", skiprows=1)[:,1:]
print('Loaded .csv file:')
print(points)
print('shape of the array:')
print(np.shape(points))
dim=np.shape(points)[0]

'''
#METHOD 2
reader = csv.reader(open(path+'/10_points.csv' ,"rU"), delimiter=",")
x=[]
for row in reader:
    x.append(row)
#x = list(reader)
points = np.array(x).astype('float')
print(points)
print(np.shape(points))
'''

mu=np.reshape(np.mean(points,axis=1),(10,1))    #calculating mean vector
#var=np.ndarray(shape(dim,dim),dtype='int')
var=np.zeros((dim,dim),dtype='float')   #initializing the C matrix
points=points-mu    # calculating (X-mu)
for i in range(dim):
    curr_point=np.reshape(points[:,i],(10,1))
    outer_product=np.matmul(curr_point,curr_point.T)   # calculating (X-mu).(X-mu)_transpose
    assert np.shape(outer_product)==np.shape(var)
    var+=outer_product # adding to calculate C
var=var/dim # dividing by 10 to get final value of C
print('Matrix C:')
print(var)

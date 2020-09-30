import pandas as pd
import csv
import numpy as np
import random

path='/home/satyaki/Desktop/IIT GUWAHATI/Courses/Machine Learning Laboratory/Assignments/Assignment 1'


points=np.random.randn(10,100)
print('The 100 points (each being a 10-dimensional vector):')
print(points)
print(np.shape(points))

#METHOD 1:
pd.DataFrame(points).to_csv(path+'/10_points.csv',header='None',index='None')
'''
#METHOD 2:
wtr = csv.writer(open (path+'out.csv', 'w'), delimiter=',', lineterminator='\n')
for x in points : wtr.writerow ([x])
'''

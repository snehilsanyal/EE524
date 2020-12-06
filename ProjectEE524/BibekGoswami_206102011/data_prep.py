# -*- coding: utf-8 -*-
"""
@author: Bibek
"""
import cv2
import glob
import numpy as np
import csv


# Converting the image into vectors and the predicted output
images = glob.glob("*.jpg")

x = []
y = []

for image in images:
    print(image)
    img = cv2.imread(image)
    im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    im = np.array(im)
    x.append(im.ravel())
    y.append(image)
  
x = np.array(x)

with open("train_celeb.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(x)
    
np.savetxt("labels_celeb.csv",  y, delimiter =", ",fmt ='% s')
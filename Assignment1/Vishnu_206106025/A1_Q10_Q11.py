# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 01:19:05 2020

@author: keyen
"""

# Function to write a simple csv file in this context
def filewritecsv(rows,*field):
    import csv
    from datetime import datetime
    import os      
    try:
        filename
    except:
        now=datetime.now()
        filename=now.strftime("Random_%d%y%H%M%S%f.csv")     
    try:
        field
    except:
        field=next(rows)        
    with open(filename, 'w') as csvfiles:
        csvwriter = csv.writer(csvfiles)
        csvwriter.writerow(field)
        csvwriter.writerows(rows)
    writefilename="%10s\\%10s" %(os.getcwd(),filename)
    return writefilename



#Function to read csv files
def filereadcsv(filename):
    import csv
    from numpy import genfromtxt
    fields=[]
    rows=[]
    with open(filename, 'r') as csvfile:
        csvreader=csv.reader(csvfile)
        fields = next(csvreader)
        key=genfromtxt(filename, delimiter=',')
        for row in csvreader:
            rows.append(row)            
    return fields, key

#Sample Program
import numpy as np


print("This program generates random numbers and stores them in a CSV file")

X=np.random.rand(100,10)
#writing the matrix into a file
FileName=filewritecsv(X)
print("The CSV File name and path --->  " +FileName)
#reading the matrix from the file
fields,rows=filereadcsv(FileName)

#Operations on the data
mu=np.array([sum(rows[i]) for i in range(100)])/100
Xmatrix=np.array([rows[i]-mu[i] for i in range(100)])
dotproduct=[]
for i in range(100):
    xmat=[];xmattran=[]
    xmat=Xmatrix[i]
    xmattran=np.transpose(Xmatrix[i])    
    dotproduct.append(np.dot(xmat,xmattran))

#Final product C
finalproductC=sum(dotproduct)/100
print("C = %f" %finalproductC)




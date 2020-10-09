import csv
from numpy import random 
import numpy as np
n = random.randint(1000,size=(100))
print(n)
file="File.csv"
with open(file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Numbers'])
    csvwriter.writerow(n)
import csv
from random import randrange as ran
a=[]
for x in range(100):
    a.append(ran(1,400))
with open('C:\\Users\\Lenovo\\Desktop\\points.csv','w') as points:
    file = csv.writer(points)
    for i in range(10):
        file.writerow(a)
print(len(a))



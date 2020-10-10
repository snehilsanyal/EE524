import numpy as np
i=0
mylist=[]
while(i<15):
    mylist.append(int(input()))
    i=i+1
my_array=np.array(mylist)
print("non ordered array = ",my_array)
for i in range(len(my_array)-1):
    for j in range(len(my_array)-i-1):
        if my_array[j]>my_array[j+1]:
            (my_array[j],my_array[j+1])=(my_array[j+1],my_array[j])
print("acsending order array = ",my_array)



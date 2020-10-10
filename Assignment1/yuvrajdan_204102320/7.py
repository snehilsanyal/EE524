#Q7
import numpy as np
def bubblesort( a):
    n=len(a)
    print(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=np.random.randint(1,100,15)
bubblesort(a)
print("assending order is:")
print(a)
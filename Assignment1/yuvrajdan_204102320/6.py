#Q6
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=list([4,5,8,2,1,9,22,11,56,34,15,16,14,26,21])
bubblesort(a)
print("desending order is:")
print(a)
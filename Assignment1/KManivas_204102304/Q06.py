##Program to sort a list in descending order using bubble sort and print the sorted indices

list1 = [20,85,100,2,11,75,91,15,18,21,29,22,12,19,27]

list2 = []
for i in range(len(list1)):
    temp_list = []
    temp_list.append(list1[i])
    temp_list.append(i)
    list2.append(temp_list)
    
count = 1

while count != 0:
    count = 0
    for i in range(len(list2)-1):
        if list2[i][0]<list2[i+1][0]:
            temp = list2[i]
            list2[i] = list2[i+1]
            list2[i+1] = temp
            count += 1
        else:
            continue

print("Elements of list in descending order:")
for i in range(len(list2)):
    print(list2[i][0], end=' ')
print()
print("Sorted indices of the list:")
for i in range(len(list2)):
    print(list2[i][1], end=' ')            
    




inordered_list=[]
i=0
while(i<15):
    inordered_list.append(int(input()))            #entries of list
    i=i+1


print("enterd list= ",inordered_list)
####descending order bubble short method
for i in range(len(inordered_list)-1):
    for j in range(len(inordered_list)-i-1):
        if inordered_list[j] < inordered_list[j + 1]:
            (inordered_list[j],inordered_list[j+1])=(inordered_list[j+1],inordered_list[j])                #swapping of two number



print("descending ordered list =",inordered_list)



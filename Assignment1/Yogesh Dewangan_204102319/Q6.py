#Bubble short
List=[12,15,6,7,3,0,9,23,76,45,37,87,54,21,89]
print("The given List is:\n",List)

for j in range(len(List)-1):
     print(f"the {j} iteration is")    
     for i in range(len(List)-1):
        if List[i]<List[i+1]:
            List[i],List[i+1]=List[i+1],List[i]
            print(List) 
    
import numpy as np

#Bubble Sort Function to sort array in ascending order
def BubbleSort(arr):
    n = arr.size
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
#Entering and Displaying the array
def array():
    arr = np.array([ ])
    print('__Enter the array emlements__')
    print('When done type Null or null to end the process:')
    flag = True
    i = 1
    #Entering the array
    while flag:
        print('Enter the element no.',i,':', end = ' ')
        ele = input()
        if ele == 'Null' or ele == 'null':
            flag = False
        else:
            intele = int(ele)
            arr = np.append(arr,intele)
            i+=1
    #Displaying the array
    print('\n\nThe entered array is:\n',arr)
    return arr

def main():
    arr = array()
    sort = BubbleSort(arr)
    print('\n\nThe sorted array is:\n',sort)

if __name__ == '__main__':
    main()

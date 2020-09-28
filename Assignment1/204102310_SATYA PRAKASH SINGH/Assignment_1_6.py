def createList():
    List = []
    print('Enter element no.:')
    for i in range(1, 16):
        print(i,'.',end = ' ')
        elem = int(input())
        List.append(elem)
    return List

def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def main():
    l = createList()
    print('\n\nThe entered list is:')
    for i in range(len(l)):
        print('%d' %l[i], end = ' ')
    sortl = BubbleSort(l)
    print('\n\nThe Sorted list is: ')
    for i in range(len(sortl)):
        print('%d' %sortl[i], end = ' ')

if __name__ == '__main__':
    main()

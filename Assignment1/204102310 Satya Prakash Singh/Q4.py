#Fermat's Little theorem
def isPrime(n):
    flag = False
    p = ((2**n)-2)%n
    if p == 0:
        flag = True
    return flag

def main():
    print('__Program to find prime numbers in range [a,b]__')
    num1 = int(input('Enter the lower limit of the range: '))
    num2 = int(input('Enter the upper limit of the range: '))
    print('The prime numbers in the give range are:')
    for i in range(num1,num2+1):
        flag = isPrime(i)
        if flag == True:
            print(i, end= ' ')
            pos = i+1
    print(pos)

if __name__ == '__main__':
    main()

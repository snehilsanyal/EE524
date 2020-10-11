def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    print('The sum of two numbers is: ',num1 + num2)
    print('The difference of two numbers is: ',num1 - num2)
    print('The product of two numbers is: ',num1 * num2)
    try:
        print('The quotient of two numbers is: ',num1 / num2)
        print('The remainder of two numbers is:', num1 % num2)
    except:
        print('The division and remainder operations cannot be performed')

if __name__ == '__main__':
    main()

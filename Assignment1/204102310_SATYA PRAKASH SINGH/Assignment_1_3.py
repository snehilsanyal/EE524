def factorial(n):
    assert n>=0
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
def main():
    num = int(input('Enter the number whose factorial is to be found:'))
    fact = factorial(num)
    print('The Factorial of the number is: ',fact)

if __name__ == '__main__':
    main()

import math

def sieve(limit):
    primes=[] #initialising a list to hold all the primes in (2,limit]
    mark=[False for i in range(limit+1)]    #initialising the sieve of Eratosthenes as all False, i.e., all primes
    for i in range(2,limit+1):
        if mark[i]==False:
            primes.append(i) # must be prime if marked False
        for j in range(i,limit+1,i):
            mark[j]=True    #marking all the multiples of i as not prime
    return primes

def primes_in_range(low,high):
    limit=math.floor(math.sqrt(high))+1
    primes=sieve(limit)     #finding the primes upto (square-root of high), which can be the highest factor of any number in the given range
    n=high-low+1
    mark=[False for i in range(n)] #initialising the sieve of Eratosthenes as all False, i.e., all primes

    for i in range(len(primes)):    #iterating over the primes upto sq-rt of high and cancelling their multiples in the given range from the sieve
        lowestMultiple=math.floor(low/primes[i])*primes[i]  #finding the highest mulitple of prime[i] just below 'low'
        if(lowestMultiple<low):
            lowestMultiple+=primes[i]   #  finding the lowest multiple of prime[i]
        if(lowestMultiple==primes[i]):
            lowestMultiple+=primes[i]
        for j in range(lowestMultiple,high+1,primes[i]):
            mark[j-low]=True    #marking the multiples as not prime

    for i in range(low,high+1): # printing the primes in the given range
        if mark[i-low]==False and (i!=1 and i!=2): # since 1 and 2 are not primes
            print(i,end=' ')
    print()


low=int(input('Enter the lower limit:'))
high=int(input('Enter the upper limit:'))
print(f'The primes in the range [{low},{high}] are:')
primes_in_range(low,high)   #printing the primes in the range [low,high]

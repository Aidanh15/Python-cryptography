#Program to generate a prime number

#Some backgroudn on prime numbers:
# Prime number is a number that by itself has only two factors, itself and 1
# As all even numbers are multiples of two, 2 is the only possible even prime number.
# Multiplying two primes together should result in a number whose only factors are 1 itself and the teo prime numbers that were multiplied. e.g 3*7 = 21, factors of 21: 1, 3, 7, 21
# A non prime number is called a composite number.
# every composite number has a prime factorization, which is a factorization comprised only of prime numbers.
#e.g 1386 has a prime factorization of 2*3*7*11


#List of functions:

# isPrimeTrialDiv() uses the trial division algorithm to return True if the number passed to it is prime, false if not.
# primeSieve() uses the sieve of Eratosthenes to generate primes.
# rabinMiller() uses the R-M algorithm to to check prime, works quicker on larger primes than trial div.
# isPrime() self explanatory combo of above
# generateLargerPrime() returns a very large prime hundreds of digits long.

#prime sieve

import math, random

def isPrimeTrialDiv(num):
#Nums less than 2 are not prime
    if num < 2:
        return False

# see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False  #0 and 1 != primes
    sieve[1] = False

    #create sieve
    for i in range(2, int(math.sqrt(sieveSize))+ 1):
        pointer = i * 2 
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # list of primes:
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)


    return primes

def rabinMiller(num):
        #T if num is prime
        if num % 2 == 0 or num < 2:
            return False #R-M doesnt work on even nums

        if num ==3:
            return True
        s = num -1
        t = 0 

        while s % 2 == 0:
            s = s // 2  #Keep halving until it is odd and use t to count how many times we halve.
            t += 1

        for trials in range(5): #try to falsify nums prime status 5 times
            a = random.randrange(2, num-1)
            v = pow(a, s, num)
            if v != 1: 
                i = 0 
                while v != (num -1):
                    if i == t - 1:
                        return False
                    else: 
                        i = i + 1
                        v = (v ** 2) % num
        return True
        
# One quick and dirty hack is to try divide by the first few dozen primes, this isquicker thn R-M but not as comprehensive

LOW_PRIMES = primeSieve(100)

def isPrime(num):
    # This does quick check first before calling R-M function
    if(num<2): 
        return False
    
    for prime in LOW_PRIMES:
        if (num % prime == 0):
            return False
    # if this fails then:
    return rabinMiller(num)

def generateLargePrime(keysize = 1024):
    while True:
        num = random.randrange(2**(keysize - 1), 2 **(keysize))
        if isPrime(num):
            return num

#TEST
#print(generateLargePrime())
#print(isPrime(159844224725405367836113564031148640387885141081192006619755805101298083823684721268614320152389860743198892070813869413262236125556820107630279749998247733276487919639358368328068783874524787646830623447079448376689120387460662921510470544268389313952089375324622435630708094749966089033301140613645616441413))
#print(isPrime(1))
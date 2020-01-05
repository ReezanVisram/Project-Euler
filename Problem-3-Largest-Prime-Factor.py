# Project Euler Problem 3
# What is the largest prime factor of the number 600851475143 ?

import math

# Defines a function that checks if a given number is prime
def isPrime(n):
    if (n == 1):
        return True

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True

largeNumber = 600851475143
goalNumber = math.floor(math.sqrt(largeNumber)) # The max value we have to iterate up to
primes = []
j = 0

# Iterates through all numbers to see if they are a factor - If they are, check if they are prime
for x in range(1, goalNumber):
    if (largeNumber % x == 0):
        if (isPrime(x)):
            primes.append(x)

print(primes[len(primes) - 1])


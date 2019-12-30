# Project Euler Problem 10
# Find the sum of all the primes below two million.
targetNumber = 2000000
total = 0

# A function using the Sieve of Erathostenes to determine all prime numbers below a certain value
def SieveOfErathostenes(n):
    global total
    prime = [True for i in range(n + 1)]

    p = 2

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            total += p
    print(total)
n = targetNumber
SieveOfErathostenes(n)

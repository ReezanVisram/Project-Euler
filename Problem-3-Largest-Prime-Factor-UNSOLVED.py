# UNSOLVED

targetNumber = 600851475143
currHighestFactor = 1

def SieveOfErathostenes(n):
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
            print(p)
            if (targetNumber % p == 0):
                if (p > currHighestFactor):
                    currHighestFactor = p

    print(currHighestFactor)

n = targetNumber
SieveOfErathostenes(n)

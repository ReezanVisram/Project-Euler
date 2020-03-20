def isPrime(n):
    if (n == 1):
        return True

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True

currNum = 0
currLargePrime = 0 

for i in range(1, 1000001):
    if (isPrime(i)):
        currNum += i

        if (isPrime(currNum)):
            if currNum > currLargePrime:
                currLargePrime = currNum


print(currLargePrime)

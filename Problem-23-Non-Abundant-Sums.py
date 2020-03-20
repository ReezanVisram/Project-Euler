def determineAbundant(n):
    divisors = []

    for i in range(1, n):
        if (n % i == 0):
            divisors.append(n / i)

    if (sum(divisors) > n):
        return n

        

abundants = []
for i in range(1, 28123):
    abundants.append(determineAbundant(i))


print(abundants)

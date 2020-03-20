def getSumOfDivisors(n):
    divisorsSum = 0

    for i in range(1, n):
        if (n % i == 0):
            divisorsSum += i

    return divisorsSum


total = 0
amicableNumbersList = []
for i in range(1, 10000):  
    sum1 = getSumOfDivisors(i)

    sum2 = getSumOfDivisors(sum1)

    if ((sum2 == i) and (sum1 != i)):
        amicableNumbersList.append(i)
        amicableNumbersList.append(sum2)

noDuplicateList = list(dict.fromkeys(amicableNumbersList))

print(sum(noDuplicateList))

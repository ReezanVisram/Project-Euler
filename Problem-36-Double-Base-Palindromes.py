import math
listPal = []
def isPal(n):
    if (str(n) == str(n)[::-1]):
        return True

    else:
        return False


def convertToDec(n):
    binValue = []
    while n > 0:
        tempVal = n % 2
        binValue.append(tempVal)
        n = math.floor(n / 2)

    binValBackward = binValue[::-1]
    finalBinNum = ''.join(str(x) for x in binValBackward)
    return finalBinNum


for i in range(1, 1000001):
    if (isPal(i)):
        if (isPal(convertToDec(i))):
            listPal.append(i)


print(sum(listPal))
        

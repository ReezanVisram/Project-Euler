import math
currTerm = 1000
numberDivisors = 0

while numberDivisors <= 500:
    numberDivisors = 0
    currTriangleNum = (currTerm * (currTerm + 1)) / 2

    highestPossFactor = math.floor(currTriangleNum / 2)
    
    for i in range(1, highestPossFactor):
        if (currTriangleNum % i == 0):
            numberDivisors += 1
    
    currTerm += 1

print(currTriangleNum)



# Project Euler Problem 28
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Intializing variables to store the necessary values
numbers = 1001
bottomLeftToTopRightList = [1]
topLeftToBottomRightList = [1]
numberIncrements = 0
incrementNum = 1

# Loops through the bottom left to top right diagonal using the pattern that the difference
# between the two numbers an equal distance away from the origin have a difference of 2x their distance from the origin
for i in range(1, numbers):
    bottomLeftToTopRightList.append(bottomLeftToTopRightList[i - 1] + (2 * i))

total = sum(bottomLeftToTopRightList) - 1

# Loops through the top left to bottom right diagonal using the pattern that the difference
# between the two numbers an equal distance away from the origin have a difference of 2x their distance from the origin twice
for i in range(1, numbers):
    if (numberIncrements >= 2):
        numberIncrements = 0
        incrementNum += 1
        
    if (numberIncrements < 2):
        topLeftToBottomRightList.append(topLeftToBottomRightList[i - 1] + (4 * incrementNum))
        numberIncrements += 1

total += sum(topLeftToBottomRightList)
print(total)    

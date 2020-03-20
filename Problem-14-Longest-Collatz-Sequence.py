currLongestSequence = 0
currLongestNum = 0
for i in range(1000001):
    currNum = i
    currSequence = 0

    while (currNum > 1):
        if (currNum % 2 == 0):
            currNum = currNum / 2
            currSequence += 1

        else:
            currNum = 3 * currNum + 1
            currSequence += 1

    if (currSequence > currLongestSequence):
        currLongestSequence = currSequence
        currLongestNum = i
print(currLongestNum)

    

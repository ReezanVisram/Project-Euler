i = 0
while True:
    numSameDigits = 0
    numsPassed = 0
    i += 1

    digitsInNum = [x for x in str(i)]

    for j in range(1, 7):
        tempInt = i * j

        for y in str(tempInt):
            if (y in digitsInNum):
                numSameDigits += 1


        if (numSameDigits == len(digitsInNum)):
            numsPassed += 1

        else:
            break

    if (numsPassed >= 6):
        break


print(i)

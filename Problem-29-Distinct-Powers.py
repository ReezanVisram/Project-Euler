distinctNumList = []

for i in range(2, 101):
    for j in range(2, 101):
        currNum = i**j

        if currNum in distinctNumList:
            continue

        else:
            distinctNumList.append(currNum)

print(len(distinctNumList))

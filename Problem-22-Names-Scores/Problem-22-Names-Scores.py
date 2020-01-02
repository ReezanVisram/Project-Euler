names = []
overallTotal = 0
currentNameTotal = 0
letterVals = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
with open('names.txt', 'r') as f:
    for x in f:
        names = x.split(',')

names.sort()

for i in range(len(names)):
    currentNameTotal = 0
    for x in str(names[i]):
        for key in letterVals:
            if key == x:
                currentNameTotal += letterVals[key]
            

    currentNameTotal = currentNameTotal * (i + 1)
    overallTotal += currentNameTotal
print(overallTotal)

# Project Euler Problem 17
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# Uses the library num2words
from num2words import num2words
total = 0

# Loops through every number between 1 and 1000
for i in range(1, 1001):
    # Strips unnecessary characters
    currNum = num2words(i)
    currNum = currNum.strip(' ')
    currNum = currNum.strip('-')

    # Checks if the unecessary characters stil exist
    for x in currNum:
        if (x == " ") or (x == "-"):
            continue

        # Adds the number of characters
        else:
            total += 1

print(total)

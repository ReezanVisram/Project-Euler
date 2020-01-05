# Project-Euler Problem 20
# Find the sum of the digits in the number 100!

# A recursive factorial function (Could have used the math library)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Assigns 100! to a variable
num = factorial(100)

total = 0
# Goes through 100! and adds up the total
for i in str(num):
    total += int(i)

print(total)

# Project Euler Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSquares = 0 # Stores the sum of each number squared
total = 0 # Stores the sum of all the numbers

# Loops through the first 100 integers
for i in range(101):
    sumOfSquares += i ** 2 
    total += i 

squareOfSums = total ** 2 

diff = squareOfSums - sumOfSquares
print(diff)

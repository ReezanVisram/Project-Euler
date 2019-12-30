# Project Euler Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

total = 0 # Stores the sum of the even fibonacci numbers
fibIndex = 0
currentFibonacciNumber = 1

# Recursive Fibonacci Function to determine the nth fibonacci term
def fibonacci(n):
    if n < 1:
        return n
    else:    
        return (fibonacci(n - 1) + fibonacci(n - 2))

maxValue = 4000000

# Loops to find all fibonacci numbers less than 4 million
while currentFibonacciNumber < maxValue:
    fibIndex += 1 # Variable that stores 'n'
    currentFibonacciNumber = abs(fibonacci(fibIndex)) # Gets the current fibonacci number

    # If the number is divisible by 2 add it to the total
    if (currentFibonacciNumber % 2 == 0):
        total += currentFibonacciNumber

print("The final total is", total)


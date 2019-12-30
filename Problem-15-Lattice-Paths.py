# Project Euler Problem 15
# How many such routes are there through a 20×20 grid?

# Recursive Factorial Function
def factorial(n):
    if n == 1:
        return n

    else:
        return n * factorial(n - 1)


# Uses a formula to find all binary permutations (Assigning 0 to moving down, 1 to moving right)
i = (factorial(40)) / (factorial(20) ** 2)
print(i)

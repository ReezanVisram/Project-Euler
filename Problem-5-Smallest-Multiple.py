# Project Euler Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Starts off the counter at 20
i = 20

""" Loops until the number is divisible by everything between 1 and 20 (Didn't have to check all numbers because if that number times 2 is less than 20,
and a number is divisible by that product, it is automatically divisible by the inital number. E.g if a number is divisible by 20, it is automatically divisible by 10 """
while (i % 11 != 0) or (i % 12 != 0)  or (i % 13 != 0) or (i % 14 != 0) or (i % 15 != 0) or (i % 16 != 0) or (i % 17 != 0) or (i % 18 != 0) or (i % 19 != 0) or (i % 20 != 0):
    i += 20

print(i)

# Project Euler Problem 16
# What is the sum of the digits of the number 2^1000?
num = 2 ** 1000
total = 0

for i in str(num):
    total += int(i)

print(total)

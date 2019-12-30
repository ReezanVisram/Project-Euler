# Project Euler Problem #1
# Find the sum of all the multiples of 3 or 5 below 1000

total = 0 # Store the current total of all multiples

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i
        
print(total)

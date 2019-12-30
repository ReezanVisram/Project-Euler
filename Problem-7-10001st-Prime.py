# Project Euler Problem 7
# What is the 10 001st prime number?

start = 2 # Defines the starting prime value
end = 90000000 # Defines the ending (Just a random large number to ensure the program doesn't stop)

currentCount = 1 # Stores the current prime number index
val = start # Defines the value

# Loops until the prime value is larger than the end (Never happens)
while val <= end:

    # Checks if the number is not prime
    if val > 1:
        for n in range(2, val):
            if (val % n == 0):
                break

        # If the number is prime add its index 
        else:
            currentCount += 1

    # Determine the next number to check
    val += 1
    
    # Break once reached the 10 001st prime number
    if (currentCount >= 10002):
        break

print(val)



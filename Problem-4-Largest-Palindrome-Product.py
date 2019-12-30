# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.

currentHighestPalindrome = 0 
currentNum = 900 # Starts the algorithm off at 900 since it is likely that the two numbers are greater than 900

# Loops through every possible number between 900 and 999 to determine if their product is a palindrome
while currentNum <= 999:
    for i in range(900, 999):
        currentNumCheck = currentNum * i

        # Checks if the product is a palindrome
        if (str(currentNumCheck) == str(currentNumCheck)[::-1]):
            # If it is, checks if the product is higher than the previous highest palindrome
            if (currentNumCheck > currentHighestPalindrome):
                currentHighestPalindrome = currentNumCheck

    currentNum += 1
    
print(currentHighestPalindrome)

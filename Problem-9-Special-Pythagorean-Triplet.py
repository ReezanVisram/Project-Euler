# Project Euler Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# A function to determine Pythagorean Triplets up to a certain limit
def pythagoreanTriplets(limits) : 
    c, m = 0, 2

    # Since a < b < c, if c becomes greater than the limit, there are no more triplets
    while c < limits:
        # Increments n until m and uses a formula to find the triplets
        for n in range(1, m): 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            if c > limits : 
                break

            # If the triplet adds to 1000 print their product
            if (a + b + c == 1000):
                print(a * b * c)
  
        m = m + 1
pythagoreanTriplets(1000)

# UNSOLVED
def factorial(n):
    if n == 1:
        return n

    else:
        return n * factorial(n - 1)

def factors(x):
    result = []

    i = 1

    while i ** 2 <= x:
        if (x % i == 0):
            result.append(i)

        if (x // i != i):
            result.append(x//i)

        i += 1

    return result

fact20 = factorial(20)
print(fact20)

print(factors(fact20) / 380)

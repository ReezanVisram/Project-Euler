def findFactors(num):
    n = num
    i = 2
    p = 1

    if (num == 1):
        return 1

    while (i**2 <= n):
        c = 1
        while (n % i == 0):
            n /= i
            c += 1

        i += 1
        p *= c


    if (n == num or n > 1):
        p *= 1 + 1

    return p

def solve(x):
    n = 1
    d = 1

    while (findFactors(d) <= x):
        n += 1
        d += n

    return d


print(solve(500))
    

    

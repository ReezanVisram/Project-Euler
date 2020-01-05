def fibonacci(n):
    arr = [i for i in range(n + 1)]

    arr[0] = 0
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return int(arr[n])

n = 2
while True:
    n += 1

    if (len(str(fibonacci(n))) >= 1000):
        break

print(n)

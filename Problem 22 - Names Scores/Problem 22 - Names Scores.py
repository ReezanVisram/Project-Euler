names = []
total = 0
values = {chr(i): i + 1 for i in range(ord("a"), ord("a") + 26)}
with open('names.txt', 'r') as f:
    for x in f:
        names = x.split(',')

names.sort()

for i in names:
    for x in str(i):
        break
    break

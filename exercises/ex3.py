lst = []
N = 10

for x in range(1, N + 1):
    if x % 3 > 0:
        lst.append(x ** 2)

print(lst)

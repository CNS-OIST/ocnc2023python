x = 5987

if x > 0 and x % 1 == 0:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
else:
    print('x is not a positive integer')
print(x)

x = 5987

if x > 0 and x % 1 == 0:
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        print(x)
else:
    print('x is not a positive integer')

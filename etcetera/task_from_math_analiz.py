# б
for n in range(1, 1001):
    if ((n**3 + 11 * n) % 6) == 0:
        if n == 1000:
            print('True')

# в
for n in range(1, 1001):
    if ((n**3 + 3 * n**2 + 5 * n + 3) % 3) == 0:
        if n == 1000:
            print('True')

# г
for n in range(1, 1001):
    if ((11 ** (n + 1) + 12 ** (2 * n - 1)) % 19) == 0:
        if n == 1000:
            print('True')

# a
for n in range(1, 1500):
    if (n * (2 * n**2 - 3 * n + 1) % 6) == 0:
        if n == 1400:
            print('True')
from collections import Counter


def n_to_p(n, p):
    r = ''
    while n > 0:
        r = '0123456789ABCDEF'[n % p] + r
        n //= p
    return r


print(n_to_p(255, 16))
print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))
print(Counter(n_to_p(49**7 + 7**21 - 7, 7)))
def alg(n):
    s1 = f'{n:b}'
    if sum(map(int, s1)) % 2 == 0:
        s2 = '10' + s1[2:] + '0'
    else:
        s2 = '11' + s1[2:] + '1'
    return int(s2, 2)


print(alg(6))
print(alg(4))

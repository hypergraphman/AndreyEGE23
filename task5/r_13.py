for n in range(1, 1000):
    st1 = f'{n:b}'
    st2a = st1 + str(st1.count('1') % 2)
    st2b = st2a + str(st2a.count('1') % 2)
    r = int(st2b, 2)
    if r > 77:
        print(n)
        break
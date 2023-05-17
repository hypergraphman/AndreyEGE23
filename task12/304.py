for x in range(30):
    for y in range(30):
        for z in range(30):
            if 3 * x + y + 7 * z == 104 and x + 3 * z == 39 and 2 * x + y + 6 * z == 83:
                print(x + y + z + 2)
                print(x, y, z)
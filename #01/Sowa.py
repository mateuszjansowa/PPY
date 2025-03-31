numbs = [256, 81, 256, 82, 27, 16807, 456]
divis = [16, 3, 8, 9, 3, 7, 4]

def isPower(x, y):
    if x == 1:
        return y == 1

    pow = 1
    while (pow < y):
        pow *= x

    if (pow == y):
        print(str(y) + " is a power of " + str(x))
        return True
    else:
        print(str(y) + " is not a power of " + str(x))
        return False


for i in range(len(numbs)):
    isPower(divis[i], numbs[i])
a = int(input())
b = int(input())


def sum(a, b):
    if b == 0:
        return a
    if b == 1:
        return a + 1
    else:
        return sum(a, b - 1) + 1


print(sum(a, b))

a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    print(min(min(a, b), min(a, c), min(a, d), min(b, c),
              min(b, d), min(d, c)))


min4(a, b, c, d)

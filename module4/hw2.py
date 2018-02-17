import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def distance(x1, y1, x2, y2):
    print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


distance(x1, y1, x2, y2)

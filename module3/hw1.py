import math

a = float(input())
b = float(input())
c = float(input())

p = 0.5 * (a + b + c)


print(math.sqrt(p * (p - a) * (p - b) * (p - c)))

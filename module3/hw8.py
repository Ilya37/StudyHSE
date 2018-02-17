a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = (f - c * e / a) / (d - c * b / a)
    x = (e - b * y) / a

print(x, y)

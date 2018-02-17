import math
a = float(input())
b = float(input())
c = float(input())

D = b*b-4*a*c
if D > 0 and a > 0:
    X2 = (-b+math.sqrt(D))/(2*a)
    X1 = (-b-math.sqrt(D))/(2*a)
    print(X1, X2)
elif D > 0 and a < 0:
    X2 = (-b+math.sqrt(D))/(2*a)
    X1 = (-b-math.sqrt(D))/(2*a)
    print(X2, X1)
elif a == 0:
    X = -b / c
    print(X)
elif D == 0:
    X = -b/(2*a)
    print(X)

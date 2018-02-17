a, b, c = int(input()), int(input()), int(input())

if a >= b >= c:
    print(a)
elif a >= c >= b:
    print(a)
elif c >= a >= b:
    print(c)
elif c >= b >= a:
    print(c)
elif b >= a >= c:
    print(b)
elif b >= c >= a:
    print(b)

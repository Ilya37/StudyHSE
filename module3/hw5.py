import math

t = float(input())

if t - int(t) >= 0.5:
    print(math.ceil(t))
elif t - int(t) < 0.5:
    print(math.floor(t))

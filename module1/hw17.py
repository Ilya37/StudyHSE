v = int(input())
t = int(input())

print(abs(v*t) % 109 if v > 0 else (109 - abs(v*t) % 109))

i = int(input())
a = []
while i != 0:
    a.append(i)
    i = int(input())
a = sorted(a)
print(a[-2])

a = []

for i in input().split():
    a.append(i)

for i in range(1, len(a)):
    if int(a[i-1]) < int(a[i]):
        print(a[i])

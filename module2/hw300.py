count = 99999999
n1 = 0
n2 = 0
i = 0
lastI = 0
step = 0
n = 0

while True:
    n2 = n1
    n1 = n
    n = int(input())
    if n == 0:
        break

    if n2 != 0 and n1 > n2 and n1 > n:
        if lastI != 0:
            step = i - lastI
            if step < count:
                count = step
        lastI = i
    i += 1

if step == 0:
    print(0)
else:
    print(count)

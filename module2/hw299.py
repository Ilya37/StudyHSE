count = 0
n1 = 0
i = 0
n = 0
step1 = 0
step2 = 0

while True:
    n1 = n
    n = int(input())
    if n == 0:
        break

    if abs(n1) > abs(n):
        step1 += 1
        count = max(count, step1)
    elif abs(n1) < abs(n):
        step2 += 1
        count = max(count, step2)
    elif abs(n1) == abs(n):
        step1 = 0
        step2 = 0
    i += 1

print(count)

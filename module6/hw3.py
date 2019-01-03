s, n = input().split()
s = int(s)
n = int(n)

volume = sorted([int(input()) for i in range(n)])
amount = sum(volume)
while amount > s and n:
    amount -= volume.pop()
    n -= 1
print(n)

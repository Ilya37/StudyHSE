n = int(input())
i, seqSum = 0, 0
while i <= n:
    seqSum = seqSum + i**2
    i += 1
print(seqSum)

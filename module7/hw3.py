used1 = list(map(int, input().split()))

used = set()
for i in used1:
    n = int(i)
    if n in used:
        print('YES')
    else:
        print('NO')
        used.add(n)

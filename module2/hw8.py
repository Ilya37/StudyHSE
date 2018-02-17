m = int(input())
n = int(input())
k = int(input())

if k < n * m and (k % m == 0 or k % n == 0):
    print('YES')
else:
    print('NO')

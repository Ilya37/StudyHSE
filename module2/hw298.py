x = int(input())
y = int(input())

print('YES' if y % (y - x + 1) == 0 else 'NO')

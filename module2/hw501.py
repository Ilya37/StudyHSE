a = int(input())
b = int(input())
c = int(input())

print(min(a, b, c))
print(min(max(a, b), max(a, c), max(b, c)))
print(max(a, b, c))

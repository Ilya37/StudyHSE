e = list(map(int, input().split()))
f = list(map(int, input().split()))

e.extend(f)
print(' '.join(map(str, sorted(e))))

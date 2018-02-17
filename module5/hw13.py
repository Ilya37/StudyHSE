a = [int(i) for i in input().split()]
b = a.index(min(a))
c = a.index(max(a))
a[c], a[b] = a[b], a[c]
print(' '.join([str(i) for i in a]))

# s = set(input().split())
# t = set(input().split())
#
# print(' '.join(str(x) for x in sorted(s.intersection(t))))

a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
c = list(a & b)
c.sort()
print(' '.join([str(i) for i in c]))

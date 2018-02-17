s = input()
if s.count('f') > 0:
    a = s.find('f')
    b = s.find('f', a+1)
    print(b)
else:
    print(-2)

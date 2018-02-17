x = float(input())
y = float(input())
p = 0.1
counter = 1

while x < y:
    x += x * p
    counter += 1
print(counter)

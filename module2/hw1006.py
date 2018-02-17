list_numbers = []
while True:
    i = int(input())
    if i == 0:
        break
    list_numbers.append(i)
print(list_numbers.count(max(list_numbers)))

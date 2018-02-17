import math

days = 0
nights = 0

h, a, b = int(input()), int(input()), int(input())

print(1 + math.ceil((h-a) / (a-b)))

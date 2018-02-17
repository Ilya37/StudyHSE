import math

n = int(input())


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    sqrtOfNumber = math.sqrt(n)

    while i <= sqrtOfNumber:
        if n % i == 0:
            return False
        i = i + 2

    return True


if isPrime(n) is True:
    print("YES")
else:
    print("NO")

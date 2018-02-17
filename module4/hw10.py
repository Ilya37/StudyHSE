import fractions

n = int(input())
m = int(input())


def ReduceFraction(n, m):
    f = fractions.Fraction(n, m)
    p = f.numerator
    q = f.denominator
    print(p, q)


ReduceFraction(n, m)

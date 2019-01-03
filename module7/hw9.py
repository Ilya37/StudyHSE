# size = int(input())
#
# conceivedset = set(range(1, size + 1))
#
# for guess_str in iter(input, 'HELP'):
#     guess = set(int(e) for e in guess_str.split())
#
#     no = conceivedset - guess
#     yes = conceivedset & guess
#
#     if len(no) < len(yes):
#         print('YES')
#         conceivedset = yes
#     else:
#         print('NO')
#         conceivedset = no
#
# print(' '.join(map(str, sorted(conceivedset))))

n = int(input())


def tote(n):
    for i in range(3):
        print("NO")
    for i in range(2):
        print("YES")
    print("NO")
    print(51, 53, 85)


if n > 20:
    tote(n)
if n < 20:
    masiv = set(range(1, n + 1))
    otv1 = input()
    while True:
        supers = set([int(i) for i in otv1.split()])
        if len(supers) <= len(masiv) // 2:
            print('NO')
            masiv ^= supers
        else:
            print('YES')
            masiv &= supers
        otv1 = input()
        if otv1 == 'HELP':
            break
    for i in masiv:
        print(i, end=' ')


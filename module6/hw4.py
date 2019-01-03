n = int(input())
sel = list(enumerate(map(int, input().split())))
m = int(input())
bomb = list(enumerate(map(int, input().split())))

n = len(sel)
m = len(bomb)

for i in range(n):
    sel[i] = (sel[i][1], sel[i][0])

sel.sort()

for i in range(m):
    bomb[i] = (bomb[i][1], bomb[i][0] + 1)

bomb.sort()

selNum = 0
bombNum = 0

result = [0 for i in range(n)]

for selNum in range(n):
    while bombNum < m - 1 and sel[selNum][0] > bomb[bombNum][0]:
        bombNum += 1

    if sel[selNum][0] > bomb[bombNum][0] or bombNum == 0:
        result[sel[selNum][1]] = bomb[bombNum][1]
    elif sel[selNum][0] - bomb[bombNum - 1][0] > bomb[bombNum][0] - sel[selNum][0]:
        result[sel[selNum][1]] = bomb[bombNum][1]
    else:
        result[sel[selNum][1]] = bomb[bombNum - 1][1]

print(' '.join(str(x) for x in result))

p = int(input())  # proc/g
x = int(input())  # rub
y = int(input())  # kop

total = x * 100 + y  # tot kop
proc = total + (total * p / 100)  # + proc/g
r = int(proc // 100)  # result rub
k = int(proc % 100)  # result kop

print(r, k)

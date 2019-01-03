from itertools import islice

kub_anna = []
kub_boris = []
kub_anna_set = set()
kub_boris_set = set()
f = open('input.txt', 'r', encoding='utf8')
first_line = f.readline().split()
n = int(first_line[0])
m = int(first_line[1])
f1 = islice(f, 0, n)
f2 = islice(f, 0, n+m)

for line in f1:
    kub_anna.append(int(line))
    kub_anna_set = set(kub_anna)

for line1 in f2:
    kub_boris.append(int(line1))
    kub_boris_set = set(kub_boris)

with open('output.txt', 'w') as file:
    for i in (kub_anna_set & kub_boris_set,
          kub_anna_set - kub_boris_set,
          kub_boris_set - kub_anna_set):
            print(len(i), file=file)
            print(*(sorted(i)), file=file)

N, M = [int(i) for i in input().split()]
kub_anna = set(int(input()) for _ in range(N))
kub_boris = set(int(input()) for _ in range(M))
with open('output.txt', 'w') as file:
    for i in (kub_anna & kub_boris,
              kub_anna - kub_boris,
              kub_boris - kub_anna):
        print(len(i), file=file)
        print(*(sorted(i)), file=file)

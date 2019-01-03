infile = open('input.txt', 'r', encoding='utf8')
outfile = open('output.txt', 'w', encoding='utf8')
lines = infile.readlines()
lines.sort()
for line in lines:
    print(*line.split()[:2] + line.split()[3:], file=outfile)

infile.close()
outfile.close()

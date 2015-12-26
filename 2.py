
i = open('inputs/2').read()

sq = 0
for line in i.split('\n'):
    f = sorted([int(x) for x in line.split('x')])
    sq += 3 * f[0] * f[1] + 2 * f[0] * f[2] + 2 * f[1] * f[2]

print(sq)
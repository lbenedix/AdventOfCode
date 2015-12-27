
def parse_line(s):
    l = s.split(' ')

    o = ''
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    if l[0] == 'toggle':
        o = 'toggle'
        x1 = int(l[1].split(',')[0])
        y1 = int(l[1].split(',')[1])
        x2 = int(l[3].split(',')[0])
        y2 = int(l[3].split(',')[1])
    else:
        if l[1] == 'on':
            o = 'on'
        elif l[1] == 'off':
            o = 'off'
        x1 = int(l[2].split(',')[0])
        y1 = int(l[2].split(',')[1])
        x2 = int(l[4].split(',')[0])
        y2 = int(l[4].split(',')[1])

    return o, x1, y1, x2, y2

    # turn off 60,313 through 75,728
    # turn on 899,494 through 940,947
    # toggle 832,316 through 971,817

size = 1001
map = [[0 for x in range(size)] for x in range(size)]


for l in open('inputs/6').read().split('\n'):
# for l in ['turn off 499,499 through 500,500']:
    o, x1, y1, x2, y2 = parse_line(l)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):

            s = map[x][y]

            if o == 'on':
                map[x][y] = 1
            elif o == 'off':
                map[x][y] = 0
            else:
                map[x][y] = 0 if s == 1 else 1


n = 0
for row in map:
    n += sum(row)
print(n)
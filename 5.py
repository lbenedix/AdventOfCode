input = open('inputs/5').read()

def nice(l):
    v = 0
    c_ = ''
    d = False

    for i in range(len(l)):
        c = l[i]

        if c in ['a','e','i','o','u']:
            v += 1

        if (c_ + c) in ['ab', 'cd', 'pq', 'xy']:
            return False

        if c_ == c:
            d = True

        c_ = c

    if v >= 3:
        return d

    return False


c = 0
for l in input.split('\n'):
    if nice(l):
        c += 1


print(c)


tests = [
    'ugknbfddgicrmopn',
    'aaa',
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb',
]

for w in tests:
    print(nice(w), w)
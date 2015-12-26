from hashlib import md5


for i in range(999999999):
    m = md5('iwrupvqb{}'.format(str(i)).encode('ascii'))

    h = m.hexdigest()

    if(h[0:5] == '00000'):
        print(i, 'abcdef{}'.format(str(i)).encode('ascii'), h[0:5])
        break



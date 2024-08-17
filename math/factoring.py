''' Factoring Algorithms '''
''' by Karl Zander '''

def factor(n):
    d = 2
    r = 1
    while r != 0:
        r = n % d
        if r != 0:
            d += 1
    v = n // d
    return d, v

''' Factors to the smallest prime factors '''
''' Produces a list of tuples '''

def zfactor(n):
    d = 2
    r = 1
    f = []
    while r != 0:
        r = n % d
        if r != 0:
            d += 1
    v = n // d
    f.append((d, v))
    while d == 2:
        d, v = factor(v)
        f.append((d, v))
    t = 0
    for x in range(0, len(f) - 1):
        t += f[x][1]
    a = f[len(f) - 1][0]
    b = f[len(f) - 1][1]
    t = (t + (a * b))
    verified = False
    if t == n:
        verified = True
    return f, verified

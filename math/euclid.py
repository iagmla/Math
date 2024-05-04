''' Euclidean algorithms '''
''' by Karl Zander '''

def gcd(a, b):
    while  b != 0:
        try:
            a = a % b
        except ZeroDivisionError:
            break
        else:
            a, b = b, a
    return a

def inverse(a, n):
    r0 = n
    r1 = a
    t0 = 0
    t1 = 1
    while r1 != 0:
        q = r0 // r1
        t0, t1 = t1, t0 - q * t1
        r0, r1 = r1, r0 - q * r1
    if r0 > 1:
        return 0
    if t0 < 0:
        t0 = t0 + n
    return t0

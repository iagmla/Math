''' Zander Algorithms '''
''' by Karl Zander '''

from euclid import inverse

''' Zander Primality Test '''

def is_prime(n):
    iters = 1000
    if n < iters:
        iters = n
    zcount = 0
    for i in range(2, iters):
        v = inverse(i, n)
        if v == 0:
            zcount += 1
    if zcount == 0:
        return True
    return False

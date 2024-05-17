''' Factoring Algorithms '''
''' by Karl Zander '''

def factor(n):
    d = 2
    r = 1
    while r != 0:
        x = n // d
        r = n % d
        if r != 0:
            d += 1
    v = n // d
    return d, v

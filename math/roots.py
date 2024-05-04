''' Roots '''
''' by Karl Zander '''

def integer_sqrt(n):
    a = n
    b = (a + n // a) // 2
    while b < a:
        a = b
        b = (a + n // a) // 2
    return b

def sqrt(n):
    a = n
    b = (a + n / a) / 2
    while b < a:
        a = b
        b = (a + n / a) / 2
    return b

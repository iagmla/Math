''' Zander Algorithms '''
''' by Karl Zander '''

def is_prime(n):
    a = n
    a = (a * a) + 2
    b = pow(a, n - 1, n)
    if b == 1:
        return True
    return False

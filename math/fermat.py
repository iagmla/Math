''' Fermat Algorithms '''
''' by Karl Zander '''

def is_prime(n):
    count = 0
    for x in range(1, 25):
        z = pow(x, n - 1, n)
        if z == 1:
            count += 1
    if count > 20:
        return True
    return False

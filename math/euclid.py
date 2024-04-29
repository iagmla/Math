''' Euclidean algorithms '''
''' by Karl Zander '''

def gcd(a, b):
    while a != 0 or b != 0:
        try:
            a = a % b
        except ZeroDivisionError:
            break
        else:
            a, b = b, a
    return a

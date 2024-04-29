import math

''' Triangular Math lib '''
''' by Karl Zander '''

def get_nth_triangular(n):
    return (n * (n + 1)) // 2

def is_triangular(n):
    t = (int(math.sqrt((8 * n) + 1) - 1)) // 2
    if t % 2 == 0:
        return True
    return False

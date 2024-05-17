''' Group Algorithms '''
''' by Karl Zander '''

def is_quadratic_residue(q, n):
    x = (q * q)
    if x == (q % n):
        return True
    return False

def is_congruent_mod_n(a, b, n):
    x = a - b
    y = n % x
    if y < 0:
        y += n
    if y == 0:
        return True
    return False

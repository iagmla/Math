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

''' Generate N bit Integer '''
''' Bit Length must be divisible by 8 '''
''' Cannot be greater than Python default maximum of 4300 bits '''

def nbit_integer(n):
    num_bytes = n // 8
    f = open("/dev/urandom", "rb")
    b = f.read(num_bytes)
    f.close()

    x = 0
    p = (len(b) * 8) - 8
    for i in range(len(b)):
        x += b[i] << p
        p -= 8
    return x

''' Generate N bit Prime '''
''' Bit Length must be divisible by 8 '''
''' Cannot be greater than Python default maximum of 4300 bits '''

def nbit_prime(n):
    x = nbit_integer(n)

    while not is_prime(x):
        x += 1
    return x

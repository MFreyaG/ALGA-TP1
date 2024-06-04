import time

from math import ceil, sqrt

def mod_inverse(a, m):
    for i in range(1, m):
        if (((a % m) * (a % m)) % m == 1):
            return i
    return -1

def bsgs(g,a,p):
    start_time = time.time()
    mod_size = len(bin(p-1)[2:])

    m = ceil(sqrt(p-1))
    # Baby Step
    lookup_table = {pow(g, j, p): j for j in range(m)}
    # Giant Step pre-computation
    c = pow(g, m*(p-2), p)
    # Giant Steps
    for i in range(m):
        temp = (a*pow(c, i, p)) % p
        if temp in lookup_table:
            # x found
            return i*m + lookup_table[temp]
        
        if time.time() - start_time > 120:
            return None

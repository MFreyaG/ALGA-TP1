import time

from miller_rabin import MillerRabin
from gen_int import phi
from bsgs import bsgs

miller_rabin = MillerRabin()
n, a = int(input()), int(input())
p = n+1

start = time.time()
iter_number = 0
while 1:
    if (p % 2 == 1):
        result = miller_rabin.main(p, 1)
        if result == 1:
            break
        else:
            iter_number += 1
            p += 1
    p += 1

print(p)

g = phi(p)
print(g)

log = bsgs(g, a, p)
print(log)

total_time = (time.time()-start) * 10**3
print(f'{total_time}ms')
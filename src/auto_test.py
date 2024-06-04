import sys
import time

from miller_rabin import MillerRabin
from gen_int import phi
from bsgs import bsgs

input_filename = sys.argv[1]
input_file = open(f'tests/input/{input_filename}', 'r')

output_filename = sys.argv[2]
output_file = open(f'tests/output/{output_filename}', 'w')

test_case = 1
while 1:
    miller_rabin = MillerRabin()
    
    try:
        x,y = int(input_file.readline()), int(input_file.readline())
    except:
        break
    
    p = x+1

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

    print(f'Test case {test_case}:')
    print(p)

    g = phi(p)
    print(g)

    log = bsgs(g, y, p)
    print(log)
    
    total_time = (time.time()-start) * 10**3
    print(f'{total_time}ms\n')
    
    output_file.write(f"{x} {p} {g} {log} {total_time}\n")
    
    if log == None:
        print(f'Test case {test_case} error: Tempo de execução ultrapassou o limite de 5 minutos, encerrando programa')
        break
    
    test_case += 1
    
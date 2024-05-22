from miller_rabin import MillerRabin

miller_rabin = MillerRabin()
n, a = int(input()), int(input())
p = n+1

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
            
print(f'Menor primo "p" maior que "n": {p}')
print(f'Miller-Rabin executado {iter_number} vezes')
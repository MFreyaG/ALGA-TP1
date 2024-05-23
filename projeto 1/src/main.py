import time
from miller_rabin import MillerRabin, find_generator, discrete_log


miller_rabin = MillerRabin()
n, a = int(input("Digite um número inteiro: ")), int(input("Digite um número inteiro para calcular o logaritmo discreto: "))
p = n + 1

iter_number = 0
while True:
    if p % 2 == 1:
        result = miller_rabin.main(p, 1)  # Teste de Miller-Rabin com k = 1
        if result == 1:
            break
        else:
            iter_number += 1
    p += 1

print(f'Menor primo "p" maior que "n": {p}')
print(f'Miller-Rabin executado {iter_number} vezes')

# Encontra um gerador de Zp
g = find_generator(p)
print(f"Um gerador de Z_{p} é: {g}")

# Calcula o logaritmo discreto com tempo limite (opcional)
try:
    start_time = time.time()
    log_result = discrete_log(g, a, p)
    end_time = time.time()

    if log_result is not None:
        print(f"O logaritmo discreto de {a} na base {g} módulo {p} é: {log_result}")
        print(f"Tempo de cálculo: {end_time - start_time:.2f} segundos")
    else:
        print("Não foi possível calcular o logaritmo discreto em tempo hábil.")
except TimeoutError as e:
    print(e)

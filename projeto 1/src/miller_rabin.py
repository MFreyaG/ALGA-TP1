import random
import time
from sympy import isprime, factorint, mod_inverse, primitive_root
from math import gcd, sqrt

class MillerRabin:
    def get_sd(self, n:int):
        s = 0
        d = n - 1
        
        while d % 2 == 0:
            d //= 2
            s += 1
        
        return s, d
    
    def get_random(self, n:int):
        return random.randint(2, n-2)
    
    def get_x(self, d:int, a:int, n:int):
        return pow(a, d, n)
    
    def main(self, n:int, k:int):
        if n <= 1:
            return 0
        if n <= 3:
            return 1
        
        s, d = self.get_sd(n)
        
        for _ in range(0, k):
            a = self.get_random(n)
            x = self.get_x(d, a, n)
            
            if x == 1 or x == n-1:
                continue
            
            for _ in range(0, s-1):
                x = pow(x,2) % n
                if x == n-1:
                    break
            else: 
                return 0

        return 1

def is_prime(n, k=5):
    """
    Teste de primalidade de Miller-Rabin com otimizações.
    """
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False
    return MillerRabin().main(n, k)

def find_next_prime(n):
    """
    Encontra o menor número primo maior que n.
    """
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def find_generator(p):
    """
    Encontra um gerador do grupo multiplicativo Zp.
    """
    return primitive_root(p) 

def baby_step_giant_step(g, h, p):
    """
    Algoritmo Baby-step Giant-step para calcular o logaritmo discreto.
    """
    m = int(sqrt(p)) + 1
    baby_steps = {pow(g, i, p): i for i in range(m)}
    giant_stride = mod_inverse(pow(g, m, p), p)

    for j in range(m):
        y = (h * pow(giant_stride, j, p)) % p
        if y in baby_steps:
            return j * m + baby_steps[y]
    return None

def pollard_rho(g, h, p):
    """
    Algoritmo Pollard's Rho para calcular o logaritmo discreto.
    """
    def f(x):
        return (x**2 + 1) % p

    x = y = random.randint(1, p - 1)
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), p - 1)

    if d == p - 1:
        return None  # Falha ao encontrar o logaritmo

    a_diff = 0
    b_diff = 0
    original_x = x
    original_y = y

    while x != y:
        x = f(x)
        y = f(f(y))
        a_diff = (a_diff + 1) % (p - 1)
        b_diff = (b_diff + 2) % (p - 1)

    a_total = (a_diff - b_diff) % (p - 1)
    b_total = (original_y - original_x) % (p - 1)

    logarithm = (mod_inverse(a_total, p - 1) * b_total) % (p - 1)
    return logarithm

def pohlig_hellman(g, h, p):
    """
    Algoritmo Pohlig-Hellman para calcular o logaritmo discreto.
    """
    factors = factorint(p - 1)
    x = 0
    for q, e in factors.items():
        gamma = pow(g, (p - 1) // q, p)
        h_i = pow(h, (p - 1) // q**e, p)
        x_i = 0
        for i in range(e):
            exp = x_i * q**(e - 1 - i)
            gamma_exp = pow(gamma, exp, p)
            h_j = (h_i * mod_inverse(gamma_exp, p)) % p
            x_j = baby_step_giant_step(gamma, h_j, p)
            x_i += x_j * q**i
        x = (x + x_i * ((p - 1) // q**e)) % (p - 1)
    return x

def discrete_log(g, h, p, timeout=300):
    """
    Calcula o logaritmo discreto com tempo limite e otimizações.
    """
    start_time = time.time()

    factors = factorint(p - 1)
    if p - 1 < 10**6 or all(factor <= 10**4 for factor in factors):
        result = baby_step_giant_step(g, h, p)
    else:
        if all(e == 1 for _, e in factors.items()):
            result = pohlig_hellman(g, h, p)  # Pohlig-Hellman se todos os expoentes forem 1
        else:
            result = pollard_rho(g, h, p)  # Pollard's Rho caso contrário

    end_time = time.time()
    if end_time - start_time > timeout:
        raise TimeoutError("Tempo limite excedido para o cálculo do logaritmo discreto.")
    return result

if __name__ == "__main__":
    try:
        n = int(input("Digite um número inteiro: "))
        p = find_next_prime(n)
        print(f"O menor primo maior que {n} é: {p}")

        g = find_generator(p)
        print(f"Um gerador de Z_{p} é: {g}")

        a = int(input("Digite um número inteiro para calcular o logaritmo discreto: "))

        start_time = time.time()
        log_result = discrete_log(g, a, p)
        end_time = time.time()

        if log_result is not None:
            print(f"O logaritmo discreto de {a} na base {g} módulo {p} é: {log_result}")
            print(f"Tempo de cálculo: {end_time - start_time:.2f} segundos")
        else:
            print("Não foi possível calcular o logaritmo discreto em tempo hábil.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

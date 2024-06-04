from math import sqrt
import time
 
""" Iterative Function to calculate (x^n)%p
    in O(logy) */"""
def power( x, y, p): 
 
    res = 1
 
    x = x % p # Update x if it is more 
              # than or equal to p 
 
    while (y > 0): 
 
        # If y is odd, multiply x with result 
        if (y & 1):
            res = (res * x) % p 
 
        # y must be even now 
        y = y >> 1 # y = y/2 
        x = (x * x) % p 
 
    return res 
 
# Utility function to store prime
# factors of a number 
def findPrimefactors(s, n) :

    # Removing multiples of two from N's factoration and adding 2 to the factors' set
    while (n % 2 == 0) :
        s.add(2) 
        n = n // 2

    # n must be odd at this point. So we can  
    # skip one element (Note i = i +2) 

    start_time = time.time()

    max = int(sqrt(n))

    for i in range(3, max, 2):
        max = int(sqrt(n))
        if i > max: break

        time_now = time.time() - start_time

        # if i % 625 == 0:
        #     print(f"Checking number {i} | {round(i/max, 5)}% of total | found {len(s)} primes | elapsed time: {int(time_now/60)}min {int(time_now % 60)}s")
        
        while (n % i == 0) :
            s.add(i) 
            n = n // i 
         
    if (n > 2) :
        s.add(n) 


def phi( n) :
    s = set() 

    phi = n - 1
 
    # Find prime factors of phi and store in a set 
    findPrimefactors(s, phi)
 
    # Check for every number from 2 to phi 
    for r in range(2, phi + 1): 
 
        # Iterate through all prime factors of phi. 
        # and check if we found a power with value 1 
        flag = False
        for it in s: 
 
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not 
            if (power(r, phi // it, n) == 1): 
 
                flag = True
                break
             
        # If there was no power with value 1. 
        if (flag == False):
            return r 
 
    return -1
 
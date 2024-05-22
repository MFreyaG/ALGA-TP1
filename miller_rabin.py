import random

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
        
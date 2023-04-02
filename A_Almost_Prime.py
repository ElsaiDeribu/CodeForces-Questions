
n = int(input())

def isAlmostPrime(n):
    
    d = 2
    divisors = set()
    
    while d * d <= n:
        
        while n % d == 0:
            divisors.add(d)
            n //= d
            
        d += 1
        
        if len(divisors) > 2:
            return False
        
    divisors.add(n) if n > 1 else None
    if len(divisors) == 2:    
        return True



count = 0
for i in range(1, n + 1):
    if isAlmostPrime(i):
        count += 1
    
print(count)
    
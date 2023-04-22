from collections import defaultdict;

n = int(input())
dic = defaultdict(set())

ans = []
color = 1

for i in range(2, n + 2):
    
    m = i
    n = i
    d = 2
    while d * d <= n:
        while n % d == 0:
            if 
            n //= d
        d += 1 
    if 2 <= n < m:
        res = True
    
        
    dic[color].add(i)  
    ans.append(color)
    
print(color)   
print(*ans)
    
    
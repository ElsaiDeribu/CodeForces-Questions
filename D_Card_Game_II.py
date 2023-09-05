n = int(input())

mati = sorted(list(map(int, input().split())))
ibsa = sorted(list(map(int, input().split())))
m = n - 1
i = 0
ans = 0

while m >= 0 and i < n and  mati[m] > ibsa[i]:
    
        ans += 1
        m -= 1
        i += 1
    
    
print(ans)
        
    
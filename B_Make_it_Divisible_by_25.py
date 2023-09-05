n = int(input())

mati = list(map(int, input().split())).sort()
ibsa = list(map(int, input().split())).sort()
m = 0
i = 0

for j in range(n):
    
    if mati[j] <= ibsa[j]:
        i += 1
    else:
        m += 1
        
if m >= i:
    print('NO')
else:
    print('YES')
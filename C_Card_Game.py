n = int(input())

mati = sorted(list(map(int, input().split())))
ibsa = sorted(list(map(int, input().split())))
m = 0
i = 0


l = 0
r = n - 1

while r >= 0 and l < n and  mati[m] > ibsa[i]:
    l += 1
    r -= 1
    
i = n - l
m = n - r - 1
    




# for j in range(n):
    
#     if mati[j] <= ibsa[j]:
#         i += 1
#     else:
#         m += 1
        
        
if m >= i:
    print('NO')
else:
    print('YES')
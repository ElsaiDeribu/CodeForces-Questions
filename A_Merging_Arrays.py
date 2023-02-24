n, m = map(int, input().split())

arrn = list(map(int, input().split()))
arrm = list(map(int, input().split()))
ans = []
ptrn, ptrm = 0, 0

while ptrn < n and ptrm < m:
    
    if arrn[ptrn] >= arrm[ptrm]:
        ans.append(arrm[ptrm])
        ptrm += 1
        
    else:
        ans.append(arrn[ptrn])
        ptrn += 1
        
ans.extend(arrm[ptrm:])
ans.extend(arrn[ptrn:])

print(*ans)
        
    
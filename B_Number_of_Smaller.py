n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


ans = []
ptr = 0

for i in range(m):
    while ptr < n and arr1[ptr] < arr2[i]:
        ptr += 1
        
    ans.append(ptr)
    
print(*ans)
        
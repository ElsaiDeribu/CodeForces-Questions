n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, -1, -1):
    m = i
    for j in range(i):
        if arr[j] > arr[m] and arr[j] > arr[i]:
            m = j
    if m != i: 
        diff =  arr[m] - arr[i]    
        arr[i] += diff 
        arr[m] -= diff 
        
print(*arr)

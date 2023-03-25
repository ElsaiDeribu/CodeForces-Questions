
import itertools
import bisect

t = int(input())

for _ in range(t):
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if n <= 2:
        print(0)
        continue
    
    for i in range(m):
        arr[i] -= 1
        
    arr.sort(reverse = True)
    arr = list(itertools.accumulate(arr))
    req = n - 2 # or more
    
    left = -1
    right = len(arr) - 1
    
    while left + 1 < right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= req:
            right = mid
        else:
            left = mid
    
    print(right + 1) if arr[right] >= req else print(-1)
    
    
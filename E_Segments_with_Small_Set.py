n, s = map(int, input().split())

arr = list(map(int, input().split()))

total = 0
count = 0
left = 0

for right in range(n):
    
    total += arr[right]
    
    while total - arr[left] >= s:
        total -= arr[left]
        left += 1
        
    count += (right - left + 1)
    
print(count)
    
    
    


n, s = map(int, input().split())

arr = list(map(int, input().split()))


left = 0
total = 0
count = 0

for right in range(n):
    total += arr[right]
        
    while total > s:
        total -= arr[left]
        left += 1
        
    count += right - left +  1

print(count)
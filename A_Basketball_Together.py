n, d = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

count = 0
left = 0
right = len(arr) - 1
currSum = 0

while left <= right:
    
    currSum = arr[right]
    while left < right and currSum <= d:
        currSum += arr[right]
        left += 1
        
    if currSum > d:
        count += 1
        currSum = 0
        
    right -= 1
        
print(count)
        
    


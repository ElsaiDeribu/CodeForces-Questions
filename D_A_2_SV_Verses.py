n, a, b = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
currSum = 0
count1 = 0

for right in range(n):
    currSum += arr[right]
    
    while currSum > b:
        currSum -= arr[left]
        left += 1
        
    
    count1 += (right - left + 1)
    
    
left = 0
currSum = 0
count2 = 0

for right in range(n):
    currSum += arr[right]
    
    while currSum >= a:
        currSum -= arr[left]
        left += 1
        
    count2 += (right - left + 1)
        
print(count1 - count2)
    

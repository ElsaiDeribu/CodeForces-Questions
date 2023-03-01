n = int(input())

arr = list(map(int, input().split()))

left, right = 0, len(arr) - 1


while left < right - 1:
    
    if arr[left] > arr[right]:
        arr[left] -= arr[right]
        right -= 1
        
    elif arr[left] < arr[right]:
        arr[right] -= arr[left]
        left += 1
        
    else:
        right -= 1
        left += 1
        
print(left, right)
        
        
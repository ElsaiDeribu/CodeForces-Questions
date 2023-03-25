t = int(input())

for _ in range(t):
    
    n = int(input())
    arr = list(map(int, input().split()))
    left = n
    arr.sort()
    
    for i in range(n - 1):
        
        if arr[i + 1] - arr[i] <= 1:
          left -= 1
          
    if left == 1:
        print("YES")
        
    else:
        print("NO")  
            
        
        
    
    
    
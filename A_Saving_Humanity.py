t = int(input())

for _ in range(t):
    n, m  = map(int, input().split())
    
    arr =  input()
    arr2 = []
    for chr in arr:
        arr2.append(int(chr))

    for _ in range(m):  
        peopleToRevive = set()
        
        for i in range(len(arr2)):
            
            if arr2[i] == 0:
                right = i + 1
                left = i - 1
                
                if ((right < len(arr2) and arr2[right] == 1) and (left < 0 or arr2[left] == 0) ) or  ((right >= len(arr2) or arr2[right] == 0) and (left >= 0 and arr2[left] == 1) ):
                    peopleToRevive.add(i)
                    
        for idx in peopleToRevive:
            arr2[idx] = 1
            
    ans =''.join(map(str, arr2))              
    
    print(ans)
        
                
    
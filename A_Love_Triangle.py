n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    arr[i] -= 1
    
flag = False
for i in range(len(arr)):
    temp = arr[i] 
    
    if i  == arr[arr[temp]]:
        flag = True
        break
        
if flag:
    print("YES")
else:
    print("NO")
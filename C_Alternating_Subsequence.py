t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    if len(a) == 1:
        print(a[0])
        continue
    
    l = 0
    r = 1
    ans = []
    
    while r < n:
        if a[l] * a[r] < 0:
            ans.append(a[l])
            l = r
            r += 1
        else:
            if a[l] < a[r]:
                l = r
                r += 1
            else:
                r += 1
                
    ans.append(a[l])
    print(sum(ans))
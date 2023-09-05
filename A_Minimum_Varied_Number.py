t  = int(input())
for _ in range(t):
    n = int(input())

    ans = []
    i = 9
    while n - i > 0:
        ans.append(i)
        n -= i
        i -= 1
      
    ans.append(n)  
    ans = ''.join(map(str, ans[::-1]))
    print (ans)


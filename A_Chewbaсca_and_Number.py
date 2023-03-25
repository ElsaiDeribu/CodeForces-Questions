n = list(input())
for i in range(len(n)):
    t = int(n[i])
    n[i] = min(9 - t, t)
        
n = str(int(''.join(map(str,n))))
print(n)
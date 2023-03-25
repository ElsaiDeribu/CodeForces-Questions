import itertools
n, m = map(int, input().split())

pref = [0] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())
    pref[s] += 1
    pref[e + 1] -= 1
    
pref = list(itertools.accumulate(pref))
flag = True
for i in range(n):
    if pref[i] == 0:
        print("YES")
        flag = False
        break
        
if flag:
    print("NO")
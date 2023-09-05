from collections import Counter
t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    array = list(map(int, input().split()))
    count = Counter(array)
    ans = 0
    
    for orbit in count:
        if count[orbit] > c:
            ans += c
        else:
            ans += count[orbit]
            
    print(ans)
    

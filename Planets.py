t = int(input())
from collections import Counter

for _ in range(t):
    
    n, c = map(int, input().split())
    planets = list(map(int, input().split()))
    ans = 0
    count = Counter(planets)
    
    for orbit in count:
        planets_in_that_orbit = count[orbit]
        if planets_in_that_orbit >= c:
            ans += c
        else:
            ans += planets_in_that_orbit
    
    print(ans)
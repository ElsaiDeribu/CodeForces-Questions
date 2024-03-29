t = int(input())
import heapq

for _ in range(t):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    heapq.heapify(a)
    
    for i in range(len(b)):
        smallest = heapq.nsmallest(1, a)[0]
        heapq.heappop(a)
        heapq.heappush(a, b[i])


    
    print(sum(a))
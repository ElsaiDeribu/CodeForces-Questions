from collections import defaultdict
import threading
from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def main():
    n, m = map(int, input().split())
    cost = list(map(int, input().split()))
    adjList = [[] for _ in range(n)]

    for _ in range(m):
        p1, p2 = map(int, input().split())
        adjList[p1 - 1 ].append(p2 - 1)
        adjList[p2 - 1 ].append(p1 - 1)
    
    visited = set()
    ans = 0

    def dfs(node):
        
        nonlocal minimum
        
        if not adjList[node]:
            return
        
        for n in adjList[node]:
            if n not in visited:
                minimum = min(minimum, cost[n])
                visited.add(n)
                dfs(n)
        

    
    for i in range(len(adjList)):
        minimum = float("inf")
        if i not in visited:
            minimum = min(minimum, cost[i])
            visited.add(i)
            dfs(i)
            
            ans += minimum
            
    print(ans)


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


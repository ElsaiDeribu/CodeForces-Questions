from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    adjList = defaultdict(list)
    inDeg = defaultdict(int)
    deq = deque()
    
    
    for _ in range(m):
        
        n1, n2 = map(int, input().split())
        
        adjList[n1].append(n2)
        adjList[n2].append(n1)
        inDeg[n1] += 1
        inDeg[n2] += 1
        
    for i in range(1, n + 1):
        if inDeg[i] == 1:
            deq.append(i)
     
    center = 0
    
    while deq:
        center = deq[0]
        
        for _ in range(len(deq)):
            node = deq.popleft()
            
            for child in adjList[node]:
                inDeg[child] -= 1
                if inDeg[child] == 1:
                    deq.append(child)
                    
    x = len(adjList[center])
    y = len(adjList[adjList[center][0]]) - 1
    
    print(x,y)
from collections import defaultdict, deque

n, m = map(int, input().split())

adjList = defaultdict(list)
color = defaultdict(int)
deq = deque()
visited = set()

for _ in range(m):
    
    a, b = input().split()
    
    adjList[a].append(b)
    adjList[b].append(a)


adjList[a] = 1

deq.append(a)
visited.add(a)
color[a] = 1 
flag = True

while deq and flag:
    
    for _ in range(len(deq)):
        node = deq.popleft()
        
        for child in adjList[node]:
            
            if color[child] == color[node]:
                flag = False
                break
            
            if child not in visited:
                if color[node] == 1:
                    color[child] = 2
                    
                else:
                    color[child] = 1
                    
                visited.add(child)
                deq.append(child)
                    
if flag:
    print("Yes")
else
from collections import deque


n, m , a = map(int, input().split())

arr = [list(input()) for _ in range(n)]
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
p = list(map(int, input().split()))

def isInbound(index):
    row = index[0]
    col = index[1]
    
    return 0 <= row < len(arr) and 0 <= col < len(arr[0])


currPos = [0,0]
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == 'M':
            arr[row][col] = '.'
            currPos = [row, col]
            break
            

for move in p:
    nxtR = currPos[0] + directions[move][0]
    nxtC = currPos[1] + directions[move][1]
    if isInbound((nxtR, nxtC)) and arr[nxtR][nxtC] == ".":
        currPos[0] += directions[move][0]
        currPos[1] += directions[move][1]
   
   
arr[currPos[0]][currPos[1]] = "M" 
   
 
level = deque([currPos])

currLayer = 0 
visited = set()
count = 1

while level:
    currLayer += 1
    
    for _ in range(len(level)):
        cell = level.popleft()
        
        for direction in directions:
            row = cell[0] + direction[0]
            col = cell[1] + direction[1]

            
            if isInbound((row, col)): 
                if (row, col) not in visited and arr[row][col] == '.' and  currLayer <= a:
                    count += 1
                    visited.add((row, col))
                    level.append((row,col))


print(count)


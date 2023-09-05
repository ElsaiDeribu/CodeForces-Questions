from collections import defaultdict

n, m = map(int, input().split())
size = defaultdict(tuple)

for row in range(n):
    for col in range(m):
        size[(row, col)] = 1
        
parent = {key: key for key in size.keys()}
matrix = [list(input()) for _ in range(n)]


def find(x):
    global parent
    
    while (parent[x] != x):
        parent[x] = parent[parent[x]] 
        x = parent[x] 
    return x
    # if parent[x] == x:
    #     return x
    # parent[x] = find(parent[x])

    # return parent[x]

def union(x, y):
    global parent
    repX = find(x)
    repY = find(y)

    if repY == repX:
        return

    if size[repX] < size[repY]:
        parent[repX] = repY
        size[repY] += size[repX]

    else:
        parent[repY] = repX
        size[repX] += size[repY]



for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == '.':
            if row + 1 < len(matrix) and matrix[row + 1][col] == '.':
                union((row, col), (row + 1, col))
            if col + 1 < len(matrix[row]) and matrix[row][col + 1] == '.':
                union((row, col), (row, col + 1))
            if col - 1 >= 0 and matrix[row][col - 1] == '.':
                union((row, col), (row, col - 1))
            if row - 1 >= 0 and matrix[row - 1][col] == '.':
                union((row, col), (row - 1, col)) 

ans = [['.'] * len(matrix[0]) for _ in range(len(matrix))]
                
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        s = 1
        visited = set()
        if matrix[row][col] == '*':
            if row + 1 < len(matrix) and matrix[row + 1][col] == '.' :
                if find((row + 1, col)) not in visited:
                    visited.add(find((row + 1, col)))
                    s += size[find((row + 1, col))]
            if col + 1 < len(matrix[row]) and matrix[row][col + 1] == '.' :
                if find((row, col + 1)) not in visited:
                    visited.add(find((row, col + 1)))
                    s += size[find((row, col + 1))]
            if col - 1 >= 0 and matrix[row][col - 1] == '.' :
                if find((row, col - 1)) not in visited:
                    visited.add(find((row, col - 1)))
                    s += size[find((row, col - 1))]
            if row - 1 >= 0 and matrix[row - 1][col] == '.' :
                if find((row - 1, col)) not in visited:
                    visited.add(find((row - 1, col)))
                    s += size[find((row - 1, col))]
                    
        if matrix[row][col] == '*':        
            ans[row][col] = s % 10
        
for row in ans:
    print(*row, sep='')
            
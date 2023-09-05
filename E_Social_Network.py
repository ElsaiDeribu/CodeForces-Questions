n, m = map(int, input().split())
size = {i: 1 for i in range(1, n + 1)}
parent = {i: i for i in range(1, n + 1)}

for _ in range(m):

   

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

    for i in range(1, len(grp) - 1):

        x = grp[i]
        y = grp[i + 1]
        union(x, y)
        
    n1, n2 =  map(int, input().split())
    ans = 0

for i in range(1, n + 1):
    ans.append(size[find(i)])

print(' '.join(map(str,ans)))
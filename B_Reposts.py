from collections import defaultdict

t = int(input())
adjList = defaultdict(list)
# visited = set()

for _ in range(t):

    destination, direction, source = input().split()
    # adjList[destination.lower()].append(source.lower())
    adjList[source.lower()].append(destination.lower())


# print(adjList)


maxDepth = 0


def dfs(node, curr):
    global maxDepth
    maxDepth = max(maxDepth, curr)

    for val in adjList[node]:
        # if val not in visited:
            # visited.add(val)
        dfs(val, curr + 1)


dfs("polycarp", 1)

print(maxDepth)

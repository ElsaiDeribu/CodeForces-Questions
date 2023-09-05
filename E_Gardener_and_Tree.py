from collections import defaultdict, deque


t = int(input())

for _ in range(t):

    adjList = defaultdict(list)
    edges = defaultdict(int)

    input()
    n, k = map(int, input().split())

    if n == 1:
        if k >= 1:
            print(0)
            continue

    for _ in range(n - 1):

        a, b = map(int, input().split())

        adjList[a].append(b)
        adjList[b].append(a)

        edges[a] += 1
        edges[b] += 1

    deq = deque()

    for item in adjList:
        if edges[item] == 1:
            deq.append(item)

    count = 0

    while k and deq:
        count += len(deq)
        for _ in range(len(deq)):
            node = deq.popleft()

            for child in adjList[node]:
                edges[child] -= 1
                if edges[child] == 1:
                    deq.append(child)

        k -= 1

    print(n - count)

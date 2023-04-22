t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    acc = 1

    for l in range(len(arr)):

        while arr[l] % 2 == 0:
            arr[l] //= 2
            acc *= 2
    mx = 0
    for i in range(len(arr)):
        if arr[i] > arr[mx]:
            mx = i

    arr[mx] *= acc

    print(sum(arr))

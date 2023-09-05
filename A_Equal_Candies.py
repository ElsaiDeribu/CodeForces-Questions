t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    s = min(arr)
    s2 = s * len(arr)
    s3 = sum(arr)
    print(s3 - s2)
    
        
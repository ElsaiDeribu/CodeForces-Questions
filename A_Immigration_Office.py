n = int(input())
arr = (input().split())
q = int(input())
import bisect

for _ in range(q):
    name = input()
    
    print(bisect.bisect_left(arr, name))
    
    
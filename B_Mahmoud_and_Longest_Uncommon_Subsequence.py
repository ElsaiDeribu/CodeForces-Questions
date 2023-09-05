from collections import defaultdict
arr1 = list(input())
arr2 = list(input())

dic = defaultdict(int)
visited = defaultdict(int)

len1 = 0
for i in range(len(arr1)):
    if arr1[i] not in dic:
        len1 += 1
        visited[arr1[i]] += 1
    else:
        len1 -= visited[arr1[i]]
        
    if i < len(arr2):
        dic[arr2[i]] += 1
        
     
    
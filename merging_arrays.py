m, n = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

mergedArray = []

ptr1, ptr2 = 0, 0

while ptr1 < len(arr1) and ptr2 < len(arr2):
    
    if arr1[ptr1] >= arr2[ptr2]:
        mergedArray.append(arr2[ptr2])
        ptr2 += 1
        
    else:
        mergedArray.append(arr1[ptr1])
        ptr1 += 1
        
mergedArray += arr1[ptr1:]
mergedArray += arr2[ptr2:]

print(*mergedArray)
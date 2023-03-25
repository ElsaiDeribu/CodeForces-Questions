from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

winel = defaultdict(int)


left = 0
longest = 0
indices = [0, 0]

for right in (range(n)):
    winel[arr[right]] += 1
    
    while len(winel) > k:
        winel[arr[left]] -= 1
        if winel[arr[left]] <= 0:
            winel.pop(arr[left]) 
        left += 1
        
    if right - left + 1 >= longest:
        longest = right - left + 1
        indices[0] = left + 1
        indices[1] = right + 1
        
    
    
print(' '.join(map(str,indices)))
    
    
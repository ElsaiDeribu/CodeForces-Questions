from collections import defaultdict
dicRow = defaultdict(lambda:defaultdict(int))
dicCol = defaultdict(lambda:defaultdict(int))


r, c = map(int, input().split())
arr = [list(input()) for i in range(r)]
ans = []

for row in range(r):
    for col in range(c):
        
        dicRow[row][arr[row][col]] += 1
        dicCol[col][arr[row][col]] += 1
        
for row in range(r):
    for col in range(c):
        if dicRow[row][arr[row][col]] == 1 and dicCol[col][arr[row][col]] == 1:
            ans.append(arr[row][col])
            
print(''.join(ans))
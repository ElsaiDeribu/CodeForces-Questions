n = int(input())
from collections import defaultdict

for _ in range(n):
    
    flag = True
    dic = defaultdict(str)
    
    list_length = int(input())
    
    numbers = input().split()
    characters = input()
    
    for i in range(list_length):
        if numbers[i] in dic:
            if dic[numbers[i]] != characters[i]:
                print("NO")
                flag = False
                break
        else:
            dic[numbers[i]] = characters[i]
            
    if flag:
        print("YES")
        
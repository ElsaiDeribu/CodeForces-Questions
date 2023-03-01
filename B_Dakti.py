t = int(input())


for _ in range(t):
    phrase = list(input().split())
    
    for i in range(len(phrase)):
        for j in range(len(phrase[i])):
            if phrase[i][j].isnumeric():
                start = j
                while j < len(phrase[i]) and phrase[i][j].isnumeric():
                    j += 1
                    
                order = int(phrase[i][start: j])
                phrase[i] = (order, phrase[i][:start] + phrase[i][j:])
                    
                break
            
    phrase.sort()
    
    for i in range(len(phrase)):
        phrase[i] = phrase[i][1]
        
    print(' '.join(phrase))
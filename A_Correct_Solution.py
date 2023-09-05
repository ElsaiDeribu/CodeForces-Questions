a = list(input())
b = input()


# for i in range(len(a)):
#     if a[i] != '0':
#         break
    
# z = ['0'] * i 
# a = a[i:]
# a.extend(z)

for i in range(len(a)): 
    for j in range(i + 1,len(a)):
        
        if i == 0 and a[j] == '0':
            continue
        
        p1 = a[i] + a[j]
        p2 = a[j] + a[i]
        
        if int(p2) < int(p1):
            a[i], a[j] = a[j], a[i]


std = ''.join(a)
ans = 'WRONG_ANSWER'

if std == b:
    ans = 'OK'
    
print(ans)

    
n = int(input())

dic = { ("S", "M"): "<", ("M", "S"): ">", ("L", "M"): ">", 
       ("M", "L"): "<", ("M", "M"): "=", ("L", "S"): ">", 
       ("S", "L"): "<"  }

for i in range(n):
    size1, size2 = input().split()
    
    if size1[-1] == size2[-1] and size2[-1] == "L":
        xLen1 = len(size1[:-1])
        xLen2 = len(size2[:-1])
        if xLen1 > xLen2:
            print('>') 
        elif xLen1 < xLen2:
            print('<')
        else:
            print('=')
            
    elif size1[-1] == size2[-1] and size2[-1] == "S":
        xLen1 = len(size1[:-1])
        xLen2 = len(size2[:-1])
        if xLen1 < xLen2:
            print('>') 
        elif xLen1 > xLen2:
            print('<')
        else:
            print('=')
            
    else:
        print(dic[(size1[-1], size2[-1])])
        
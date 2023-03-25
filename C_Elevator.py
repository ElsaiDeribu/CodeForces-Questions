t = int(input())

for _ in range(t):
    w, e, f = map(int, input().split())
   
    if e <= w: 
        if (2 * f) * e <= (w * f):
            t = ((2 * f) * e ) + ((4 - f) * e)
            print(t)
            
        else:
            t = (w * f) +  ((4 - f) * e)
            print(t)
            
    else:
        t = w * 4
        print(t)

            
            
    
    
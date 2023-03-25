t = int(input())
x = 0

def fr(len):
    
    global t
    global x
    
    if t == 0:
        return
    
    nxt = input().split()
    t -= 1
    
    if nxt[0] == "end":
        return
    
    elif nxt[0] == "for":
        fr(int(nxt[1]) * len)
        if x > (2**32 - 1):
            fr(len)
        
    else:
        for i in range(len):
            if x > (2**32 - 1):
                return
            x += 1
        fr(len)

fr(1)

print(x) if x <= (2**32 - 1) else print("OVERFLOW!!!")
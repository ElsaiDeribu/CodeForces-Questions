
def solve():
    a, b = map(int, input().split())
    
    def check(num):
        
        if min(a, b) < num:
            return False
        
        return (a + b) >= 4 * num
    
    left = 0
    right = (a + b) // 4 + 1
    
    while left + 1 < right:
        mid = left + (right - left)   // 2
        
        if check(mid):
            left = mid
        else:
            right = mid
            
    print(left) 
    
    return   
    
    
t = int(input())

for _ in range(t):
    solve()
    
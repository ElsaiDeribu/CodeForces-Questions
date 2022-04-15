from math import ceil

n,m,a= list(map(int, input().split()))

def numberOfFlagstones(n, m, a):
    width = (ceil (n/a))
    height = (ceil (m/a))
    ans = (width * height)
    print(ans)
    
numberOfFlagstones(n,m,a)
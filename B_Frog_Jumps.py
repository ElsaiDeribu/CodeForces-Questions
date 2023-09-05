t = int(input())

for _ in range(t):
    string = list(input())
    minjump = 0
    frog = -1
    for i in range(len(string)):
        if string[i] == 'R':
            minjump = max(minjump, i - frog)
            frog = i
            
    minjump = max(minjump, len(string) - frog)
    print(minjump )
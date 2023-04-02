n = int(input())

arr = list(map(int, input().split()))

all_are_even = all(num % 2 == 0 for num in arr)
all_are_odd = all(num % 2 == 1 for num in arr)

if all_are_even or all_are_odd:
    print(*arr)
else:
    print(*sorted(arr))
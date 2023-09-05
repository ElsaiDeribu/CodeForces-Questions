n = int(input())
arr = list(map(int, input().split()))
moneySpent = arr[0]
profit = 0

for price in arr:
        profit = max(profit, price - moneySpent) 
        moneySpent = min(moneySpent, profit - price)

  

print(profit)
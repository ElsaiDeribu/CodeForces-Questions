from collections import defaultdict

t = int(input())

for _ in range(t):
    
    n, m =  map(int, input().split())
    
    matrix = [list(map(int, input().split())) for i in range(n)]
    
    diagonalSum1 = defaultdict(int)
    diagonalSum2 = defaultdict(int)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            diagonalSum1[col - row] += matrix[row][col]
            diagonalSum2[col + row] += matrix[row][col]
    
    maximumSum = 0
    
    for row in range(len(matrix)):
        
        for col in range(len(matrix[0])):
            firstDiagonalSum = diagonalSum1[col - row]
            secondDiagonalSum = diagonalSum2[col + row]
            cellSum = firstDiagonalSum + secondDiagonalSum - matrix[row][col]
            
            if cellSum > maximumSum:
                maximumSum = cellSum
                
                
    print(maximumSum)    
        
            
    
    
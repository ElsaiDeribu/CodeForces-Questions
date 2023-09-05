
r1,c1,r2,c2 = map(int,input().split())

minimumRookMoves = 0
minimumKingMoves = 0
minimumBishopMoves = 0

if r1 == r2 and c1 == c2:
    minimumRookMoves = 0
    minimumBishopMoves = 0
    minimumKingMoves = 0
    
elif r1 == r2 or c1 == c2:
    minimumRookMoves = 1
    minimumBishopMoves = 0
    if r1 == r2:
        minimumKingMoves = abs(c1 - c2)
    else:
        minimumKingMoves = abs(r1 - r2)

elif abs(r1 - r2) == abs(c1 - c2):
    minimumRookMoves = 2
    minimumBishopMoves = 1 
    minimumKingMoves = abs(r1 - r2)

elif abs(r1 - r2) != abs(c1 - c2):
    minimumRookMoves = 2
    minimumBishopMoves = 2
    minimumKingMoves = max(abs(r1 - r2) ,abs(c1 - c2))

    
print(minimumRookMoves, minimumBishopMoves, minimumKingMoves)

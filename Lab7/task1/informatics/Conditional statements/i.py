queen_row = int(input())
queen_col = int(input())
piece_row = int(input())
piece_col = int(input())

if (queen_row == piece_row or 
    queen_col == piece_col or 
    abs(queen_row - piece_row) == abs(queen_col - piece_col)):
    print("YES")
else:
    print("NO")

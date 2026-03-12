bishop_row = int(input())
bishop_col = int(input())
piece_row = int(input())
piece_col = int(input())

if abs(bishop_row - piece_row) == abs(bishop_col - piece_col):
    print("YES")
else:
    print("NO")

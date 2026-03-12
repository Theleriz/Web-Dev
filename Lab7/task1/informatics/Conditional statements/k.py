knight_row = int(input())
knight_col = int(input())
piece_row = int(input())
piece_col = int(input())

if (abs(knight_row - piece_row) == 2 and abs(knight_col - piece_col) == 1) or \
   (abs(knight_row - piece_row) == 1 and abs(knight_col - piece_col) == 2):
    print("YES")
else:
    print("NO")

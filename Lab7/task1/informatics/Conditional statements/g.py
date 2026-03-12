rook_row = int(input())
rook_col = int(input())
piece_row = int(input())
piece_col = int(input())

if rook_row == piece_row or rook_col == piece_col:
    print("YES")
else:
    print("NO")

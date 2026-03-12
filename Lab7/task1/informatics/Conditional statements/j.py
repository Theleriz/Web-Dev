start_col = int(input())
start_row = int(input())
end_col = int(input())
end_row = int(input())

if abs(start_col - end_col) <= 1 and abs(start_row - end_row) <= 1:
    print("YES")
else:
    print("NO")

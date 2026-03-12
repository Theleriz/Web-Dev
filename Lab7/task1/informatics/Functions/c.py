def xor(x, y):
    return (x == 1 and y == 0) or (x == 0 and y == 1)

x, y = map(int, input().split())
print(1 if xor(x, y) else 0)

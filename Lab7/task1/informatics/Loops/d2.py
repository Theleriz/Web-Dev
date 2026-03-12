N = int(input())

if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")

import math

N = int(input())

for i in range(1, math.isqrt(N) + 1):
    square = i * i
    if square <= N:
        print(square)

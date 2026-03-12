import math

a = int(input())
b = int(input())

for i in range(math.isqrt(a), math.isqrt(b) + 1):
    square = i * i
    if a <= square <= b:
        print(square)

def power(a: float, b:int):
    return a ** b

a, b = map(int, input().split())
print(power(a, b))
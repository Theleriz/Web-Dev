n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
while max_val in arr:
    arr.remove(max_val)

print(max(arr))

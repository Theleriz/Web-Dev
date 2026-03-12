k = int(input())

possible = False
for n in range(2, 30001):
    chips = 4 * (n - 1)
    if chips == k:
        possible = True
        break

print("YES" if possible else "NO")

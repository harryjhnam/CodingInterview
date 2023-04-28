mi, mx = map(int, input().split())

l = []
for i in range(2, int(mx**0.5) + 1):
  for j in range(max(1, mi // (i**2)), mx // (i**2) + 1):
    x = (i**2) * j
    if mi <= x <= mx:
      l.append((i**2) * j)

print(mx - mi - len(set(l)) + 1)

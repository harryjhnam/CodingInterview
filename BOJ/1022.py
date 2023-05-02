def get(r, c):
  if r >= 0 and -r <= c <= r:
    return (2 * r + 1)**2 - r + c
  elif c > 0 and -c <= r <= c - 1:
    return (2 * (c - 1) + 1)**2 - r + c
  elif r < 0 and r <= c <= -r - 1:
    return (2 * r - 1)**2 + 5 * r - c
  else:
    return (2 * c - 1)**2 + 3 * c + r


r1, c1, r2, c2 = map(int, input().split())

res = []
str_len = 0
for r in range(r1, r2 + 1):
  row = []
  for c in range(c1, c2 + 1):
    s = str(get(r, c))
    str_len = max(str_len, len(s))
    row.append(s)
  res.append(row)

for row in res:
  print(' '.join([" " * (str_len - len(s)) + s for s in row]))

N = int(input())

sol = 0
for h in range(N+1):
  if '3' in str(h):
    sol += 60*60
  else:
    for m in range(60):
      if '3' in str(m):
        sol += 60
      else:
        for s in range(60):
          if '3' in str(s):
            sol += 1

print(sol)
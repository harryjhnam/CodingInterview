N = int(input())
Xs = sorted( map(int, input().split()) )

n_members = 0
n_groups = 0

for X in Xs:
  n_members += 1
  if n_members >= X:
    n_members = 0
    n_groups += 1

print(n_groups)
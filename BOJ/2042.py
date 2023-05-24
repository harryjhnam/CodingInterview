# https://www.acmicpc.net/problem/2042
# 구간 합 구하기

n, m, k = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (n + 1)


def update(i, diff):
  while i <= n:
    tree[i] += diff
    i += (i & -i)


def prefix_sum(i):
  res = 0
  while i > 0:
    res += tree[i]
    i -= (i & -i)
  return res


def interval_sum(i, j):
  return prefix_sum(j) - prefix_sum(i - 1)


for i in range(1, n + 1):
  x = int(input())
  arr[i] = x
  update(i, x)

res = []
for _ in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1:
    update(b, c - arr[b])
    arr[b] = c
  else:
    res.append(interval_sum(b, c))

for r in res:
  print(r)

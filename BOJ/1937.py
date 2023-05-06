# https://www.acmicpc.net/problem/1937
# 욕심쟁이 판다

import sys

sys.setrecursionlimit(1000000)  # Recursion error 뜰 때,

n = int(input())
grid = []
for _ in range(n):
  grid.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_count(x, y):

  if dp[x][y] != -1:
    return dp[x][y]

  count = 1
  for d in range(4):
    n_x, n_y = x + dx[d], y + dy[d]
    if 0 <= n_x < n and 0 <= n_y < n and grid[x][y] < grid[n_x][n_y]:
      count = max(count, get_count(n_x, n_y) + 1)
  dp[x][y] = count

  return dp[x][y]


res = 0
for i in range(n):
  for j in range(n):
    res = max(res, get_count(i, j))

print(res)

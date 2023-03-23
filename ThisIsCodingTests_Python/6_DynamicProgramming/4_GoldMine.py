T = int(input())  # the number of test cases


def solution(n, m, mine):
  dp = []
  for _ in range(n + 2):
    dp.append([0] * m)

  for i in range(n + 2):
    dp[i][0] = mine[i][0]

  for j in range(1, m):
    for i in range(1, n + 1):
      dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
      dp[i][j] += mine[i][j]

  candidates = []
  for i in range(1, n + 1):
    candidates.append(dp[i][m - 1])
  return max(candidates)


for _ in range(T):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  mine = []
  mine.append([0] * m)
  for i in range(n):
    mine.append(array[i * m:(i + 1) * m])
  mine.append([0] * m)
  # mine : (n+2)*(m)
  print(solution(n, m, mine))

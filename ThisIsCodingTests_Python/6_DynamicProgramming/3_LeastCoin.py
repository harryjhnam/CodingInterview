N, M = map(int, input().split())

values = []
for _ in range(N):
  values.append(int(input()))

dp = [1e9] * (M + max(values))
dp[0] = 0

for i in range(1, M + 1):
  dp[i] = min([dp[i - v] for v in values]) + 1

if dp[M] >= 1e9:
  print(-1)
else:
  print(dp[M])

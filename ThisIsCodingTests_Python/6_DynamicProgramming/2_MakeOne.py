X = int(input())

dp = [1e9] * (X * 5 + 1)
dp[X] = 0

for i in range(X - 1, 0, -1):
  dp[i] = min(dp[i + 1], dp[i * 2], dp[i * 3], dp[i * 5]) + 1

print(dp[1])

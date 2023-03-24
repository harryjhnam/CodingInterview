N = int(input())
stats = list(map(int, input().split()))

# Length of longest increasing array before each element
stats.reverse()
dp = [1] * N

for i in range(1, N):
  for j in range(0, i):
    if stats[j] < stats[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

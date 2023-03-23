N = int(input())
Ks = list(map(int, input().split()))

if N <= 2:
  print(max(Ks))

else:
  dp = [0] * N
  dp[0] = Ks[0]
  dp[1] = max(Ks[:2])
  for i in range(2, N):
    dp[i] = max(Ks[i] + dp[i - 2], dp[i - 1])
  print(dp[N - 1])

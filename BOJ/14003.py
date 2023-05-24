# https://www.acmicpc.net/problem/14003
# 가장 긴 증가하는 부분 수열 5


def solution(n, seq):
  dp = [[] for _ in range(n)]
  dp[0] = [seq[0]]

  for i in range(1, n):
    max_len = 0
    for j in range(0, i):
      if dp[j] and dp[j][-1] < seq[i] and len(dp[j]) + 1 > max_len:
        dp[i] = dp[j] + [seq[i]]
        max_len = len(dp[i])

  return max(dp, key=len)


def main():
  n = int(input())
  seq = list(map(int, input().split()))
  subseq = solution(n, seq)
  print(len(subseq))
  print(' '.join(map(str, subseq)))


if __name__ == '__main__':
  main()

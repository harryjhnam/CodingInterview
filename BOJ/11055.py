# https://www.acmicpc.net/problem/11055
# 가장 큰 증가하는 부분 수열


def solution(n, seq):
  answer = 0

  dp = [0] * n
  dp[0] = seq[0]

  for i in range(1, n):
    for j in range(i):
      if seq[i] > seq[j]:
        dp[i] = max(dp[j], dp[j] + seq[i])
      else:
        dp[i] = max(dp[j], seq[j])

  return answer


def main():
  n = int(input())
  seq = list(map(int, input().split()))
  print(solution(n, seq))


if __name__ == '__main__':
  main()

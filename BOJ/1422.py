# https://www.acmicpc.net/problem/1422
# 숫자의 신

from collections import defaultdict
import heapq

K, N = map(int, input().split())

numbers = []
len2numbers = defaultdict(list)

max_len = -1
for _ in range(K):
  n = input()
  filled_n = int(n * (10 // len(n)) + n[:10 % len(n)])
  heapq.heappush(numbers, (-filled_n, n))
  heapq.heappush(len2numbers[len(n)], (-filled_n, n))
  max_len = max(max_len, len(n))

n_repeated = N - K
_, repeating_n = heapq.heappop(len2numbers[max_len])

res = ''
repeated = False
while numbers:
  _, s = heapq.heappop(numbers)
  if s == repeating_n and not repeated:
    res += s * (n_repeated + 1)
    repeated = True
  else:
    res += s

print(res)

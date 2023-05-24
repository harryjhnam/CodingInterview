# https://www.acmicpc.net/problem/2042
# 구간 합 구하기


def update_sum(int_seq, accum_sum, b, c):

  diff = int_seq[b] - c
  for i in range(b, len(accum_sum)):
    accum_sum[i] -= diff

  int_seq[b] = c

  return int_seq, accum_sum


n, m, k = map(int, input().split())
int_seq = [None]
accum_sum = [None]
accum = 0
for _ in range(n):
  i = int(input())
  int_seq.append(i)
  accum += i
  accum_sum.append(accum)

res = []
for _ in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1:
    int_seq, accum_sum = update_sum(int_seq, accum_sum, b, c)
  else:
    res.append(accum_sum[c] - accum_sum[b - 1])

for r in res:
  print(r)

# https://www.acmicpc.net/problem/1005
# ACM Craft


def solution(graph, start):

  res = 0
  return res


t = int(input())

res = []
for _ in range(t):
  n, k = map(int, input().split())

  cost = [0] + list(map(int, input().split()))

  graph = [[] * (n + 1)]
  for _ in range(k):
    prv, nxt = map(int, input().split())
    graph[nxt].append((cost[prv], prv))

  w = int(input())

  res.append(solution(graph, w))

for r in res:
  print(r)

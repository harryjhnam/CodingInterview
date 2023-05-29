# https://www.acmicpc.net/problem/2252
# 줄세우기

from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  from_n, in_n = map(int, input().split())
  graph[from_n].append(in_n)
  indegree[in_n] += 1

result = []
q = deque()

for i in range(1, N + 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  result.append(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      q.append(i)

print(' '.join([str(r) for r in result]))

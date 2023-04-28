# https://www.acmicpc.net/problem/1238
# 파티
import heapq


def daijkstra(n, graph, start):
  distance = [1e9] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in range(1, n + 1):
      if graph[now][i] == 1e9:
        continue
      new_dist = dist + graph[now][i]
      if new_dist < distance[i]:
        distance[i] = new_dist
        heapq.heappush(q, (new_dist, i))

  return distance


N, M, X = map(int, input().split())
to_party_graph = [[1e9] * (N + 1) for _ in range(N + 1)]  # reversed direction
from_party_graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  a, b, t = map(int, input().split())
  to_party_graph[b][a] = t
  from_party_graph[a][b] = t

to_party = daijkstra(N, to_party_graph, X)
from_party = daijkstra(N, from_party_graph, X)
max_dist = 0
for x, y in zip(to_party, from_party):
  if x == X or y == X:
    continue
  if x != 1e9 and y != 1e9:
    max_dist = max(max_dist, x + y)

print(max_dist)

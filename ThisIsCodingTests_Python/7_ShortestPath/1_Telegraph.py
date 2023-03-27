import heapq

N, M, C = map(int, input().split())

distance = [1e9] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))

# Dijkstra
q = []
heapq.heappush(q, (0, C))
distance[C] = 0
while q:
  dist, now = heapq.heappop(q)
  if dist > distance[now]:
    continue
  for n, c in graph[now]:
    cost = dist + c
    if cost < distance[n]:
      distance[n] = cost
      heapq.heappush(q, (cost, n))

count = 0
max_dist = 0
results = []
for dist in distance[1:]:
  if dist != 1e9:
    count += 1
    max_dist = max(dist, max_dist)

print(count-1, max(results))



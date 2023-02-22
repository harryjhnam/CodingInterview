from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
  graph.append( list( map(int, input()) ) )

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

queue = deque([(0,0)])

while queue:
  n, m = queue.popleft()
  for d in range(4):
    new_n, new_m = n + dn[d], m + dm[d]

    if new_n <= -1 or new_n >= N or new_m <= -1 or new_m >= M:
      continue

    if graph[new_n][new_m] == 1:
      graph[new_n][new_m] = graph[n][m] + 1
      queue.append((new_n, new_m))

print(graph[N-1][M-1])

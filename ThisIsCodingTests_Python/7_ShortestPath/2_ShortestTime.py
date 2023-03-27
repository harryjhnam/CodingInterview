N, M = map(int, input().split())

graph = [ [1e9]*(N+1) for _ in range(N+1) ]
for i in range(1, N+1):
  graph[i][i] = 0

for _ in range(M):
  i, j = map(int, input().split())
  graph[i][j], graph[j][i] = 1, 1

X, K = map(int, input().split())

for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

dist1 = graph[1][K]
dist2 = graph[K][X]

if dist1+dist2 >= 1e9:
  print(-1)
else:
  print(dist1+dist2)

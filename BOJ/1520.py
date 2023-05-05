m, n = map(int, input().split())
maps = []
for _ in range(m):
  maps.append(list(map(int, input().split())))

dm = [0, 0, -1, 1]
dn = [-1, 1, 0, 0]
start, end = (0, 0), (m - 1, n - 1)

dp = [[-1] * n for _ in range(m)]
dp[m-1][n-1] = 1

def get_n_routes(cm, cn):
  if dp[cm][cn] != -1:
    return dp[cm][cn]

  n_routes = 0
  for d in range(4):
    nm, nn = cm+dm[d], cn+dn[d]
    if 0<=nm<m and 0<=nn<n and maps[nm][nn] < maps[cm][cn]:
      n_routes += get_n_routes(nm, nn)

  dp[cm][cn] = n_routes

  return dp[cm][cn]

print( get_n_routes(0,0) )

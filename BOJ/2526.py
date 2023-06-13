# https://www.acmicpc.net/problem/2562
# 최댓값

m = 0
m_i = 0
for i in range(1, 10):
  x = int(input())
  if x > m:
    m = x
    m_i = i

print(m)
print(m_i)

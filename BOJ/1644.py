# https://www.acmicpc.net/problem/1644
# 소수의 연속합

n = int(input())

is_prime = [True] * (n + 1)

for i in range(2, int(n**0.5) + 1):
  if is_prime[i]:
    j = 2
    while i * j <= n:
      is_prime[i * j] = False
      j += 1

primes = [i for i in range(2, n + 1) if is_prime[i]]

total, answer = 0, 0
start = 0
for end in range(len(primes)):
  total += primes[end]

  while total > n and start < len(primes):
    total -= primes[start]
    start += 1

  if total == n:
    answer += 1
    total -= primes[start]
    start += 1
    if start >= len(primes) or start > end:
      break

print(answer)

# 시간 복잡도
# 화폐의 개수 = K 일 때 , O(K)

N = int(input())

coin_vals = [500, 100, 50, 10]

n = 0
for coin_val in coin_vals:
  n += N // coin_val
  N = N % coin_val

print(n)
